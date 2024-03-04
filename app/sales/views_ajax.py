from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F, FloatField
from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse

from app.common.utils import format_price_
from app.products.models import Product, Stock
from app.settings.models import MachineCard
from app.financial_control.models import Movements
from app.financial_control.config_html import config_html

from .models import Sale, ItemsSale
from .forms import (SaleForm, ItemForm, FormPayment, ItemPedidoForm, ListMAqCartaoForm)


class ListVendas(LoginRequiredMixin, ListView):
    paginate_by = 8
    model = Sale
    fields = '__all__'
    template_name = 'vendas/views_ajax/lista_vendas.html'
    form_filter = None

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return self.model.objects.filter(client__name_unaccent__icontains=query)
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        self.request.session['query'] = self.request.GET.get('query', None)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['sales'] = paginator.page(page)
        return context


class CreateVenda(View):
    def post(self, request):
        data = {}
        sale_form = SaleForm(request.POST or None)
        data['cliente'] = request.POST['cliente']
        data['venda_id'] = request.POST['venda_id']

        if data['venda_id']:
            sale = Sale.objects.get(id=data['venda_id'])
            sale_form = SaleForm(request.POST or None, instance=sale)

            if sale_form.is_valid():
                sale = sale_form.save(commit=False)
                return redirect('edit-pedido', venda=sale.pk)

        else:
            if sale_form.is_valid():
                sale = sale_form.save(commit=False)
                sale.seller = request.user
                sale.save()
                return redirect('edit-pedido', venda=sale.pk)
            else:
                print('erros', sale_form.errors)
                return sale_form.errors


class UpdateHeadVenda(View):
    def post(self, *args, **kwargs):
        sale = Sale.objects.get(id=kwargs['pk'])
        sale_form = SaleForm(self.request.POST or None, instance=sale)
        if sale_form.is_valid():
            sale_form = sale_form.save(commit=False)
            sale_form.save()
            return JsonResponse({
                'updated': 'True',
                'valor': sale_form.valor,
                'total_venda': format_price_(sale.calculate_total()),
                'mensagem': 'Cabeçalho da venda foi atualizado com sucesso!7'
            })
        return render(self.request, 'vendas/views_ajax/form_header.html',
                      {'form': sale_form,
                       'id_object': sale_form.pk})


class AlterStatus(View):
    def post(self, *args, **kwargs):
        new_status = self.request.POST.get('status', 0)
        sale = Sale.objects.get(id=kwargs['venda'])
        if new_status == 'cancel' or new_status == 'not_pay':
            Movements.objects.filter(type_mov=1,
                                     id_object=sale.id,
                                     movement='Venda').delete()
        sale.status = new_status
        sale.save()
        return JsonResponse({'updated': 'True',
                             'id_venda': sale.pk})


class AddItemVenda(View):
    def post(self, *args, **kwargs):
        response_data = {}
        print(self.request.POST)
        id_venda = kwargs['id_venda']
        id_produto = self.request.POST.get('produto_list', 0)
        desconto_produto = self.request.POST.get('desconto', 0)
        quantidade_produto = self.request.POST.get('quantidade', 1)
        item = ItemsSale.objects.filter(product_id=id_produto, sale_id=id_venda)

        if item:
            print("error produto já existe")
            item_add = Product.objects.get(id=id_produto)
            response_data['itens'] = {"descricao": item_add.descricao}
            response_data['result'] = "error"
            response_data['mensagem'] = 'Item já incluso no pedido, por favor edite!'
            return JsonResponse(response_data)
        elif id_produto == 0:
            print("error sem produto")
            response_data['itens'] = {"descricao": "none"}
            response_data['result'] = "error"
            response_data['mensagem'] = 'Selecione um produto na lista'
            return JsonResponse(response_data)
        else:
            produto_estoque = Stock.objects.get(product_id=id_produto)
            produto_estoque.alter_stock(id_produto, int(quantidade_produto))
            ItemsSale.objects.create(
                product_id=id_produto, quantity=quantidade_produto,
                discount=desconto_produto, sale_id=id_venda)
            sale = Sale.objects.get(id=id_venda)
            print('add item')
            response_data['result'] = "success"
            response_data['mensagem'] = "Item adicionado com sucesso"
            response_data['total_venda'] = format_price_(sale.calculate_total())
            return JsonResponse(response_data)


class EditItem(View):
    def get(self,  *args, **kwargs):
        print(kwargs['item'])
        item_order = ItemsSale.objects.get(id=kwargs['item'])
        print(item_order)
        form = ItemForm(instance=item_order)
        return render(self.request, 'vendas/views_ajax/form_edit_item.html', {
            'form': form,
            'id_object': item_order.id,
            'name_product': item_order.product.description,
            'val_product': item_order.product.price,
            'id_venda': item_order.sale.id
        })

    def post(self, *args, **kwargs):
        item_order = ItemsSale.objects.get(id=kwargs['pk'])
        form = ItemForm(self.request.POST or None, self.request.FILES or None, instance=item_order)

        if form.is_valid():
            print('form is valid')
            form = form.save(commit=False)
            form.save()
            total = item_order.venda.calculate_total()
            return JsonResponse({'updated': 'True',
                                 'id_venda': item_order.sale.pk,
                                 'total_venda': "Total: R$ " + str("%.2f" % total).replace(".", ","),
                                 'qted': item_order.quantity})
        print('form not valid')
        print(form.errors)

        return render(self.request, 'vendas/views_ajax/form_edit_item.html', {
            'form': form,
            'id_object': item_order.id,
            'name_product': item_order.product.description,
            'val_product': item_order.produto.price,
            'id_venda': item_order.sale.id
        })


class DeleteItem(View):
    def get(self, *args, **kwargs):
        item_order = ItemsSale.objects.get(id=kwargs['item'])
        return render(
            self.request, 'vendas/views_ajax/form_item_delete.html', {
                'id_object': item_order.id,
                'name_product': item_order.product.description,
            })

    def post(self, *args, **kwargs):
        item_order = ItemsSale.objects.get(id=kwargs['item'])

        produto_qted = item_order.quantity
        produto_estoque = Stock.objects.get(produto=item_order.produto)

        produto_estoque.alterar_estoque(item_order.produto, produto_qted)
        id_sale = item_order.sale.id
        total = item_order.venda.calcular_total()
        item_order.delete()
        return JsonResponse({'deleted': True,
                             'id_venda': id_sale,
                             'total_venda': format_price_(total)})


class ItemDecrementQTED(View):
    def post(self, *args, **kwargs):
        item_order = ItemsSale.objects.get(id=kwargs['item'])
        product_stock = Stock.objects.get(product=item_order.product)
        print('quantidade ', item_order.quantity)
        item_order.quantity -= 1
        item_order.save()
        product_stock.current_stock += 1
        product_stock.save()
        total = item_order.sale.calculate_total()
        print('quantidade ', item_order.quantity)
        return JsonResponse({'updated': 'True',
                             'id_venda': item_order.sale.pk,
                             'total_venda': "Total: R$ " + str("%.2f" % total).replace(".", ","),
                             'qted': item_order.quantity})


class ItemAdditionQTED(View):
    def post(self, *args, **kwargs):
        item_order = ItemsSale.objects.get(id=kwargs['item'])
        print(item_order.quantity)
        product_stock = Stock.objects.get(product=item_order.product)
        if product_stock.current_stock > 0:
            item_order.quantity += 1
            item_order.save()
            product_stock.current_stock -= 1
            product_stock.save()
            total = item_order.sale.calculate_total()
            print('estoque atual ', product_stock.current_stock)
            return JsonResponse({'updated': 'True',
                                 'id_venda': item_order.sale.pk,
                                 'total_venda': format_price_(total),
                                 'qted': item_order.quantity,
                                 'estoque_baixo': product_stock.current_stock <= product_stock.minimum_stock})
        else:
            total = item_order.sale.value
            print(item_order.quantity)
            return JsonResponse({'error': 'Estoque Vazio!',
                                 'id_venda': item_order.sale.pk,
                                 'total_venda': format_price_(total),
                                 'qted': item_order.quantity})


class ListItensVenda(View):
    def get(self, request):
        print(self.request)
        sale = Sale.objects.get(id=request.GET.get('venda_id'))
        total_sale = sale.calculate_total()
        items_sale = ItemsSale.objects.filter(sale_id=request.GET.get('venda_id'))
        return render(request, 'vendas/views_ajax/itens-vendas.html',
                      {'items_venda': items_sale,
                       'total_venda': total_sale})


def reload_itens_venda2(request):
    sale = Sale.objects.get(id=request.GET.get('venda_id'))
    total_sale = sale.calculate_total()
    items_sale = ItemsSale.objects.filter(sale_id=request.GET.get('venda_id'))
    return render(request, 'vendas/views_ajax/itens-vendas.html',
                  {'items_venda': items_sale,
                   'total_venda': total_sale})


class FormPagamentoView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        context = {}
        sale = Sale.objects.get(id=self.kwargs.get('venda'))

        total_sale = sale.itemssale_set.all().aggregate(
            total_sale=Sum((F('quantity') * F('product__price')) - F('discount'), output_field=FloatField())
        )['total_sale'] or 0
        total_sale = total_sale - float(sale.discount)

        # context = ClienteForm(instance=cliente OR None)FormPayment
        context['form_payment'] = FormPayment()
        context['form_item'] = ItemPedidoForm()
        context['ListMAqCartaoForm'] = ListMAqCartaoForm
        context['taxas_maq'] = MachineCard.objects.all().first()
        context['desconto'] = float(sale.discount)
        context['venda'] = sale
        print(sale.id)
        context['itens'] = sale.itemssale_set.all().annotate(
            total_item=Sum((F('quantity') * F('product__price')) - F('discount'), output_field=FloatField())
        )
        context['subtotal'] = sale.itemssale_set.all().aggregate(
            subtotal=Sum((F('quantity') * F('product__price')), output_field=FloatField())
        )['subtotal'] or 0

        context['total_desconto'] = (sale.itemssale_set.all().aggregate(
            total_desconto=Sum((F('discount')), output_field=FloatField())
        )['total_desconto'] or 0) + float(sale.discount)

        context['total_venda'] = total_sale
        return render(request, 'vendas/views_ajax/form_payment.html', context)

    def post(self, request, *args, **kwargs):
        sale = Sale.objects.get(id=kwargs['venda'])

        val_pix = float(request.POST['pg_pix'])
        val_money = float(request.POST['pg_card'])
        val_card = float(request.POST['pg_especie'])

        if val_pix + val_money + val_card >= sale.value > 0:
            sale.status = 'paid'
            sale.save()
            if not Movements.all_objects.filter(id_object=sale.id, movement='Venda').exists():
                Movements.objects.create(
                     user=request.user,
                     type_mov='1',
                     id_object=sale.id,
                     movement='Venda',
                     form_pg=request.POST['set_payment_methods'],
                     val_card=request.POST['pg_card'].replace(',', '.'),
                     val_card_liq=request.POST['pg_card'].replace(',', '.'),
                     val_pix=request.POST['pg_pix'].replace(',', '.'),
                     val_money=request.POST['pg_especie'].replace(',', '.'),
                     val_total=sale.value,
                     config_html=config_html['config_inputs']

                )
            else:
                Movements.all_objects.filter(id_object=sale.id, movement='Venda').update(
                    deleted_at=None
                )
            return JsonResponse({'payment': 'success'})
        else:
            return JsonResponse({'payment': 'error', 'detail': 'valor inferior a venda a ser paga'})


class CardsMachines(View):
    def get(self, *kwarg, **kwargs):
        return render(self.request, 'vendas/views_ajax/card_machines.html',
                      {'taxas_card_machines': MachineCard.objects.get(id=kwargs['id_maq'])})

    def card_machine(self, *kwarg, **kwargs):
        id_maq = self.request.GET.get("id_maq")
        return JsonResponse(MachineCard.objects.get(id=id_maq).json_export(), status=200)
