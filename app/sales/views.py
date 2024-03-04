from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core import serializers
from django.contrib.auth.models import Permission

from .models import Sale
from app.products.models import Category, Product, Stock
from app.financial_control.models import Movements
from .forms import (SaleForm, ItemPedidoForm, ProdutoAddForm, VendaFormReadOnly)

import logging


my_log = logging.getLogger('django')


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        data = {}
        data['media'] = Sale.objects.media()
        data['media_desc'] = Sale.objects.media_desconto()
        data['min'] = Sale.objects.min()
        data['max'] = Sale.objects.max()
        data['n_ped'] = Sale.objects.num_pedidos()
        return render(request, 'vendas/dashboard.html', data)


class ListaVendas(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'vendas/lista-vendas.html', {'count_vendas': Sale.objects.all().count()})


class NewVenda(LoginRequiredMixin, View):
    def get(self, request):
        data = {'form_venda': SaleForm(), 'sale': None}
        return render(request, 'vendas/create_venda.html', data)

    def post(self, request):
        print('request ',request.POST)
        vendaform = SaleForm(request.POST or None)
        if vendaform.is_valid():
            print(vendaform)
            venda = vendaform.save(commit=False)
            print(venda.id)
            venda.seller = request.user

            venda.total_discount = 0
            venda.save()
            return redirect('edit-pedido', venda=venda.pk)
        else:
            print('vendaform.errors ', vendaform.errors)
            return vendaform.errors


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        venda = Sale.objects.get(id=venda)
        data['form_produto'] = ProdutoAddForm()
        data['AddProdutoForm'] = ItemPedidoForm()
        data['desconto'] = float(venda.discount)
        data['venda'] = venda
        print(venda.id)
        data['itens'] = venda.itemssale_set.all().order_by('-created_at')
        if venda.status == 'not_pay' and not venda.is_canceled:
            vendaform = SaleForm(instance=venda or None)
            data['form_venda'] = vendaform
            return render(self.request, 'vendas/edit_venda.html', data)
        elif venda.status == 'paid' and not venda.is_canceled:
            vendaform = VendaFormReadOnly(instance=venda or None)
            data['form_venda'] = vendaform
            return render(self.request, 'vendas/edit_venda.html', data)
        else:
            vendaform = VendaFormReadOnly(instance=venda or None)
            data['form_venda'] = vendaform
            return render(self.request, 'vendas/canceled_venda.html', data)

    def post(self, request):
        data = {'cliente': request.POST['cliente'], 'venda_id': request.POST['venda_id']}
        venda = Sale.objects.get(id=data['venda_id'])
        vendaform = SaleForm(request.POST or None, instance=venda)
        if vendaform.is_valid():
            venda = vendaform.save(commit=False)
            vendaform.clean()
            return redirect('edit-pedido', venda=venda.pk)
        else:
            return render(self.request, 'vendas/edit_venda.html', {
                'form_venda': vendaform,
                'id_object': venda.id,
            })


class DeletePedido(View):
    def get(self, request, venda):
        venda = Sale.objects.get(id=venda)
        return render(
            request, 'vendas/delete-pedido-confirm.html', {'venda': venda})

    def post(self, request, venda):
        venda = Sale.objects.get(id=venda)
        Movements.objects.filter(id_moviemnto=venda.id, tipo=1).delete()
        items_sale = venda.itemssale_set.all()
        for item in items_sale:

            produto_pedido = Product.objects.get(id=item.produto.pk)
            produto_estoque = Stock.objects.get(produto=item.produto.pk)
            Qted_estoque = int(item.quantidade)

            produto_estoque.alterar_estoque(item.produto.pk, Qted_estoque)

        venda.delete()
        return redirect('lista-vendas')


def filtra_produtos(request):
    id_categoria = request.POST.get['outro_param']
    print(request.POST.get['outro_param'], 'ddd')

    categoria = Category.objects.get(id=id_categoria)

    qs_json = serializers('json', categoria.product_set.all())
    return HttpResponse(qs_json, content_type='application/json')


