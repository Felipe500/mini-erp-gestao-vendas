from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import BillsPay, BillsReceive
from .forms import ContaReceberForm, ContaPagarForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum, FloatField
from django.views.generic import ListView
from .models import Movements


class ListMovements(LoginRequiredMixin, ListView):
    paginate_by = 20
    model = Movements
    fields = '__all__'
    template_name = 'views_ajax/listas_movimentacoes.html'
    form_filter = None
    is_filtered = False

    def get_queryset(self):
        queryset = self.model.objects.all()
        type_mov = self.request.GET.get('type', None)
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)

        if type_mov:
            print('type_mov')
            queryset = queryset.filter(type_mov=type_mov)
        if start_date:
            print('start_date')
            queryset = queryset.filter(created_at__gte=start_date)
        if end_date:
            print('end_date')
            queryset = queryset.filter(created_at__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        query_set = self.get_queryset()
        paginator = self.paginator_class(query_set, self.paginate_by)

        saidas = query_set.filter(type_mov=0).aggregate(
            saidas=Sum(('val_total'), output_field=FloatField())
        )['saidas'] or 0
        entradas = query_set.filter(type_mov=1).aggregate(
            entradas=Sum(('val_total'), output_field=FloatField())
        )['entradas'] or 0

        context['total'] = "%.2f" % (entradas - saidas)
        context['entradas'] = "%.2f" % entradas
        context['saidas'] = "%.2f" % saidas

        context['entradas_pix'] = "%.2f" % 0
        context['val_cartao'] = "%.2f" % 0
        context['entradas_especie'] = "%.2f" % 0

        context['movimentos'] = paginator.page(page)
        return context


class CreateBillsPay2(LoginRequiredMixin, View):
    form_class = ContaPagarForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'views_ajax/form_conta_pagar.html', {'form': form,
                                                                    'id_object': 0})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'created': 'True'})
        else:
            print(form.errors)
            return render(request, 'views_ajax/form_conta_pagar.html', {'form': form,
                                                                        'id_object': 0})


class ChangeBillsPay2(LoginRequiredMixin, View):
    form_class = ContaPagarForm

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        bills_pay = BillsPay.objects.get(pk=pk)
        form = self.form_class(instance=bills_pay)
        return render(request, 'views_ajax/form_conta_pagar.html', {'form': form,
                                                                    'id_object': pk,
                                                                    'name_bill_pay': bills_pay.description
                                                                    })

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        bills_pay = BillsPay.objects.get(pk=pk)
        form = self.form_class(request.POST or None, instance=bills_pay)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        else:
            return render(request, 'views_ajax/form_conta_pagar.html', {'form': form,
                                                                        'id_object': pk,
                                                                        'name_bill_pay': bills_pay.description
                                                                        })


class DeleteBillsPay2(LoginRequiredMixin, View):
    form_class = ContaPagarForm

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        bills_pay = BillsPay.objects.get(pk=pk)
        form = self.form_class(instance=bills_pay)
        return render(request, 'views_ajax/delete_conta_pagar.html', {'form': form,
                                                                      'id_object': pk,
                                                                      'name_bill_pay': bills_pay.descricao})

    def post(self, *args, **kwargs):
        BillsPay.objects.get(id=kwargs['pk']).delete()
        return JsonResponse({'deleted': True})


class ViewCreateBillsPay(View):
    def get(self, request):
        form = ContaPagarForm()
        return render(request, 'views_ajax/form_conta_pagar.html', {
            'form': form,
            'id_object': 0,
            'name_bill_pay': 'Cliente Novo'
        })


class ViewUpdateBillsPay(View):
    def get(self, request, pk):
        print(pk)
        bill_pay = BillsPay.objects.get(id=pk)
        print(bill_pay)
        form = ContaPagarForm(instance=bill_pay)
        return render(request, 'views_ajax/form_conta_pagar.html', {
            'form': form,
            'id_object': bill_pay.id,
            'name_bill_pay': bill_pay.descricao
        })


class ViewDeleteBillsPay(View):
    def get(self, request, pk):
        print(pk)
        bill_pay = BillsPay.objects.get(id=pk)
        print(bill_pay)
        form = ContaPagarForm(instance=bill_pay)
        return render(request, 'views_ajax/delete_conta_pagar.html', {
            'form': form,
            'id_object': bill_pay.id,
            'name_bill_pay': bill_pay.descricao,
        })


class ListBillsPay(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = BillsPay
    fields = '__all__'
    template_name = 'views_ajax/contas_pagar.html'
    form_filter = None
    is_filtered = False

    def get_queryset(self):
        queryset = self.model.objects.all()
        query = self.request.GET.get('query', None)
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        categoria = self.request.GET.get('categoria', None)
        status = self.request.GET.get('status', None)

        if query:
            queryset = self.model.objects.filter(
                Q(descricao__unaccent__icontains=query))
        if categoria:
            print('3')
            queryset = queryset.filter(categoria=categoria)
        if status:
            print('4')
            queryset = queryset.filter(status=status)
        if start_date:
            print('111')
            queryset = queryset.filter(created_at__gte=start_date)
        if end_date:
            print('1222')
            queryset = queryset.filter(created_at__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)
        print(page)
        context['contas_pagar'] = paginator.page(page)
        return context


class ViewCreateBillsReceive(View):
    def get(self, request):
        print('dddd')
        form = ContaReceberForm()
        return render(request, 'views_ajax/form_conta_receber.html', {
            'form': form,
            'id_object': 0,
            'name_bill': 'Cliente Novo'
        })


class ViewUpdateBillsReceive(View):
    def get(self, request, pk):
        print(pk)
        bill_receive = BillsReceive.objects.get(id=pk)
        print('bill_receive - ',bill_receive)
        form = ContaReceberForm(instance=bill_receive)
        return render(request, 'views_ajax/form_conta_receber.html', {
            'form': form,
            'id_object': bill_receive.id,
            'name_bill': bill_receive.description
        })


class ViewDeleteBillsReceive(View):
    def get(self, request, pk):
        print(pk)
        bill_receive = BillsReceive.objects.get(id=pk)
        print(bill_receive)
        form = ContaReceberForm(instance=bill_receive)
        return render(request, 'views_ajax/delete_conta_receber.html', {
            'form': form,
            'id_object': bill_receive.id,
            'name_bill': bill_receive.description,
        })


class ListToReceive(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = BillsReceive
    fields = '__all__'
    template_name = 'views_ajax/contas_receber.html'
    form_filter = None

    def get_queryset(self):
        queryset = self.model.objects.all()
        query = self.request.GET.get('query', None)
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        categoria = self.request.GET.get('categoria', None)
        status = self.request.GET.get('status', None)

        if query:
            print('21')
            queryset = self.model.objects.filter(
                Q(descricao__unaccent__icontains=query))
        if categoria:
            print('3')
            queryset = queryset.filter(categoria=categoria)
        if status:
            print('4')
            queryset = queryset.filter(status=status)
        if start_date:
            print('111')
            queryset = queryset.filter(created_at__gte=start_date)
        if end_date:
            print('1222')
            queryset = queryset.filter(created_at__lte=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)
        context['contas_receber'] = paginator.page(page)
        return context