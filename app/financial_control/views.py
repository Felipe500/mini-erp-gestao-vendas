from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, View

from .models import BillsPay, BillsReceive
from .forms import ContaReceberForm, ContaPagarForm

from app.sales.models import Sale
from .models import Movements

from .filters import ContaReceberFilter, ContaPagarFilter, MovimentacoesFilter


class MovementsView(LoginRequiredMixin, ListView):
    paginate_by = 5
    context_object_name = 'Movements'
    queryset = Movements.objects.all()
    template_name = 'controle_contas/movimentacoes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data_entries = Movements.my_entries()
        data_outings = Movements.my_outings()

        outings = data_outings['outings'] or 0

        context['filters'] = MovimentacoesFilter()
        context['total'] = "%.2f" % (data_entries['val_total']-outings)
        context['entradas'] = "%.2f" % data_entries['val_total']
        context['saidas'] = "%.2f" % outings

        context['entradas_pix'] = "%.2f" % data_entries['val_pix']
        context['val_cartao'] = "%.2f" % data_entries['val_card']
        context['entradas_especie'] = "%.2f" % data_entries['val_money']

        return context


class NovaEntrada(LoginRequiredMixin, View):
    def post(self, request):
        data = {}
        venda = Sale.objects.get(id=request.POST['id_venda'])
        venda.status = ''
        venda.save()
        Movements.objects.create(user=request.user,
                                 tipo='1',
                                 id_moviemnto=venda.id,
                                 movimento='Venda',
                                 valor=venda.valor,
                                 forma_pg=request.POST['payment-methods'],
                                 val_cartao=request.POST['pg_card_input'],
                                 val_cartao_liq=request.POST['pg_card_input'],
                                 val_pix=request.POST['pg_pix'],
                                 val_transferencia=request.POST['payment-methods'],
                                 val_especie=request.POST['pg_especie'],
                                 val_total=venda.valor,
                                 )
        return render(request, 'vendas/dashboard.html', data)


# CONTAS A PAGAR
class ContaPagarListView(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = BillsPay
    fields = '__all__'
    template_name = 'controle_contas/conta_a_pagar_list.html'
    context_object_name = 'obj'

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContaPagarListView, self).get_context_data(*args, **kwargs)
        # Add in the publisher
        page = self.request.GET.get('page', 1)
        print(page)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)
        context['filters'] = ContaPagarFilter()
        context['object_list'] = paginator.page(page)
        return context


class ContaPagarCreateView(LoginRequiredMixin, CreateView):
    model = BillsPay
    form_class = ContaPagarForm
    success_url = reverse_lazy('contas_pagar_list')
    template_name = 'controle_contas/conta_a_pagar_novo.html'


class ContaPagarDeleteView(LoginRequiredMixin, DeleteView):
    model = BillsPay
    form_class = ContaPagarForm
    success_url = reverse_lazy('contas_pagar_list')
    template_name = 'controle_contas/conta_a_pagar_delete.html'


class ContaPagarUpdateView(LoginRequiredMixin, UpdateView):
    model = BillsPay
    form_class = ContaPagarForm
    success_url = reverse_lazy('contas_pagar_list')
    template_name = 'controle_contas/conta_a_pagar_form.html'


# CONTAS A RECEBER
class ContaReceberListView(LoginRequiredMixin, ListView):
    paginate_by = 8
    model = BillsReceive
    fields = '__all__'
    template_name = 'controle_contas/conta_a_receber_list.html'
    context_object_name = 'obj'

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContaReceberListView, self).get_context_data(*args, **kwargs)

        page = self.request.GET.get('page', 1)
        print(page)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)
        context['filters'] = ContaReceberFilter()
        context['object_list'] = paginator.page(page)

        # Add in the publisher

        return context


class ContaReceberCreateView(LoginRequiredMixin, CreateView):
    model = BillsReceive
    form_class = ContaReceberForm
    success_url = reverse_lazy('contas_receber_list')
    template_name = 'controle_contas/conta_a_pagar_novo.html'


class ContaReceberDeleteView(LoginRequiredMixin, DeleteView):
    model = BillsReceive
    form_class = ContaReceberForm
    success_url = reverse_lazy('contas_receber_list')
    template_name = 'controle_contas/conta_a_pagar_delete.html'


class ContaReceberUpdateView(LoginRequiredMixin, UpdateView):
    model = BillsReceive
    form_class = ContaReceberForm
    success_url = reverse_lazy('contas_receber_list')
    template_name = 'controle_contas/conta_a_pagar_form.html'
