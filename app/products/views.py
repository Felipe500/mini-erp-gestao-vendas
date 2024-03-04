from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from .models import Product, Stock, Category
from .forms import StockForm


class CategoriaList(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Category
    fields = '__all__'
    template_name = 'produtos/categoria_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['object_list'] = paginator.page(page)
        return context


class ProdutosList(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Product
    fields = '__all__'
    template_name = 'produtos/produto_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['object_list'] = paginator.page(page)
        return context


class ListStockProducts(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Stock
    fields = '__all__'
    template_name = 'produtos/estoque_produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['object_list'] = paginator.page(page)
        return context


class editar_estoque(LoginRequiredMixin, UpdateView):
    model = Stock
    form_class = StockForm
    success_url = reverse_lazy('estoque_produtos')
    template_name = 'produtos/estoque_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['id_product'] = self.get_object().produto.descricao
        return context

