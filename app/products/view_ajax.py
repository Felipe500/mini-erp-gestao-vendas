from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from django.core import serializers

from .models import Product, Stock, Category
from .forms import (ProductForm, ProductFormReadOnly,
                    NewProductForm, StockForm, AddStockForm, CategoryForm,
                    OutputStockForm)


class ViewProduct(LoginRequiredMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductFormReadOnly(instance=product)
        return render(request, 'views_ajax/form_product.html', {'form': form})


class CreateProduct(View):
    def get(self, request):
        form = NewProductForm()
        return render(request, 'views_ajax/form_product.html', {
            'form': form,
            'id_product': 0,
            'name_product': 'Cliente Novo'
        })

    def post(self,  *args, **kwargs):
        form = NewProductForm(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            print('valid')
            current_stock = form.cleaned_data['current_stock']
            minimum_stock = form.cleaned_data['minimum_stock']
            form = form.save(commit=False)
            form.save()
            Stock.objects.create(product_id=form.id, current_stock=current_stock, minimum_stock=minimum_stock)
            return JsonResponse({'created': 'True'})
        print('not valid')
        print(form.errors)
        return render(self.request, 'views_ajax/form_product.html', {
            'form': form,
            'id_product': 0,
            'name_client': 'novo produto',
        })


class UpdateProduct(View):
    def get(self, request, pk):
        print(pk)
        product = Product.objects.get(id=pk)
        print(product)
        form = ProductForm(instance=product)
        return render(request, 'views_ajax/form_product.html', {
            'form': form,
            'id_product': product.id,
            'name_product': product.description
        })

    def post(self,  *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        form = ProductForm(self.request.POST or None, self.request.FILES or None, instance=product)

        if form.is_valid():
            print('form is valid')
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        print('form not valid')
        return render(self.request, 'views_ajax/form_product.html', {
            'form': form,
            'id_product': product.id,
            'name_product': product.description
        })


class UpdateStockProduct(View):
    def get(self, request, pk):
        print(pk)
        stock_product = Stock.objects.get(id=pk)
        print(stock_product)
        form = StockForm(instance=stock_product)
        return render(request, 'views_ajax/form_stock_product.html', {
            'form': form,
            'id_object': stock_product.id,
            'name_product': stock_product.product.description
        })

    def post(self,  *args, **kwargs):
        stock = Stock.objects.get(id=kwargs['pk'])
        form = StockForm(self.request.POST or None, self.request.FILES or None, instance=stock)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        print(form.errors)
        return render(self.request, 'views_ajax/form_stock_product.html', {
            'form': form,
            'id_object': stock.id,
            'name_product': stock.product.description
        })


class DeleteProduct(View):
    def get(self, request, pk):
        print(pk)
        product = Product.objects.get(id=pk)
        print(product)
        form = ProductForm(instance=product)
        return render(request, 'views_ajax/product_delete.html', {
            'form': form,
            'id_product': product.id,
            'name_product': product.description,
        })

    def post(self,  *args, **kwargs):
        Stock.objects.filter(product__id=kwargs['pk']).delete()
        Product.objects.get(id=kwargs['pk']).delete()
        return JsonResponse({'deleted': True})


class AddStockProduct(View):
    def get(self, request,  *args, **kwargs):
        stock_product = Stock.objects.get(id=kwargs['pk'])
        print(stock_product)
        form = AddStockForm()
        return render(request, 'views_ajax/form_add_stock.html', {
            'form': form,
            'id_object': stock_product.id,
            'value_stock': stock_product.current_stock,
            'name_product': stock_product.product.description
        })

    def post(self,  *args, **kwargs):
        stock = Stock.objects.get(id=kwargs['pk'])
        form = AddStockForm(self.request.POST or None)

        if form.is_valid():
            estoque_atual = form.cleaned_data['add_stock']
            print(estoque_atual)
            stock.current_stock += int(estoque_atual)
            stock.save()
            return JsonResponse({'updated': 'True'})

        return render(self.request, 'views_ajax/form_add_stock.html', {
            'form': form,
            'id_object': stock.id,
            'value_stock': stock.estoque_atual,
            'name_product': stock.product.description
        })


class OutputStockProduct(View):
    def get(self, request,  *args, **kwargs):
        stock_product = Stock.objects.get(id=kwargs['pk'])
        print(stock_product)
        form = OutputStockForm()
        return render(request, 'views_ajax/form_output_stock.html', {
            'form': form,
            'id_object': stock_product.id,
            'value_stock': stock_product.current_stock,
            'name_product': stock_product.product.description or 'none'
        })

    def post(self,  *args, **kwargs):
        stock = Stock.objects.get(id=kwargs['pk'])
        form = OutputStockForm(self.request.POST or None)

        if form.is_valid():
            estoque_atual = form.cleaned_data['output_stock']
            print(estoque_atual)
            stock.current_stock -= int(estoque_atual)
            stock.save()
            return JsonResponse({'updated': 'True'})

        return render(self.request, 'views_ajax/form_output_stock.html', {
            'form': form,
            'id_object': stock.id,
            'value_stock': stock.current_stock,
            'name_product': stock.product.description
        })


class CreateCategory(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'views_ajax/form_category.html', {
            'form': form,
            'id_category': 0,
            'name_category': 'Nova Categoria'
        })

    def post(self,  *args, **kwargs):
        form = CategoryForm(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'created': 'True'})
        return render(self.request, 'views_ajax/form_category.html', {
            'form': form,
            'id_client': 0,
            'name_client': 'Nova Categoria',
        })


class UpdateCategory(View):
    def get(self, request, id):
        print(id)
        category = Category.objects.get(id=id)
        print(category)
        form = CategoryForm(instance=category)
        return render(request, 'views_ajax/form_category.html', {
            'form': form,
            'id_category': category.id,
            'name_category': category.name
        })

    def post(self,  *args, **kwargs):
        print(kwargs['id'])
        category = Category.objects.get(id=kwargs['id'])
        print(category)
        form = CategoryForm(self.request.POST or None, self.request.FILES or None, instance=category)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        print(form.errors)
        return render(self.request, 'views_ajax/form_category.html', {
            'form': form,
            'id_product': category.id,
            'name_product': category.name
        })


class DeleteCategory(View):
    def get(self, request, id):
        print(id)
        category = Category.objects.get(id=id)
        print(category)
        form = CategoryForm(instance=category)
        return render(request, 'views_ajax/category_delete.html', {
            'form': form,
            'id_category': category.id,
            'name_category': category.name
        })

    def post(self,  *args, **kwargs):
        Category.objects.get(id=kwargs['id']).delete()
        return JsonResponse({'deleted': True})


class ListProductsAjax(LoginRequiredMixin, ListView):
    paginate_by = 8
    model = Product
    fields = '__all__'
    template_name = 'views_ajax/get_list_products.html'
    form_filter = None

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return self.model.objects.filter(description__unaccent__icontains=query)
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        self.request.session['query'] = self.request.GET.get('query', None)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['object_list'] = paginator.page(page)
        return context


class ListStockProductsAjax(LoginRequiredMixin, ListView):
    paginate_by = 8
    model = Stock
    fields = '__all__'
    template_name = 'views_ajax/get_list_stock.html'
    form_filter = None

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return self.model.objects.filter(product__description__unaccent__icontains=query)
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['object_list'] = paginator.page(page)
        return context


class ListCategoryProductsAjax(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = Category
    fields = '__all__'
    template_name = 'views_ajax/get_list_category.html'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return self.model.objects.filter(name__unaccent__icontains=query)
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['object_list'] = paginator.page(page)
        return context


class ProductsByCategory(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        if kwargs['id_category']:
            categoria = Category.objects.get(id=kwargs['id_category'])
            qs_json = serializers.serialize('json', categoria.produto_set.all())
        else:
            qs_json = serializers.serialize('json', Product.objects.all())
        return HttpResponse(qs_json, content_type='application/json')


