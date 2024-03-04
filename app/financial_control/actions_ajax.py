from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import BillsPay, BillsReceive
from .forms import ContaReceberForm, ContaPagarForm


class CreateBillsPay(View):
    def post(self, request, *args, **kwargs):
        form = ContaPagarForm(request.POST or None)
        if form.is_valid():
            # form.cleaned_data["descricao"]
            print('form is valid')
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'created': 'True'})
        print('form not valid')
        return render(self.request, 'views_ajax/form_conta_pagar.html', {
            'form': form,
            'id_object': 0,
            'name_client': 'novo cliente',
        })


class UpdateBillsPay(View):
    def post(self, *args, **kwargs):
        billspay = BillsPay.objects.get(id=kwargs['pk'])
        form = ContaPagarForm(self.request.POST or None, self.request.FILES or None, instance=billspay)
        if form.is_valid():
            print('form is valid')
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        print('form not valid')
        return render(self.request, 'views_ajax/form_conta_pagar.html', {
            'form': form,
            'id_object': billspay.id,
            'name_client': billspay.nome_completo
        })


class DeleteBillsPay(View):
    def post(self, *args, **kwargs):
        BillsPay.objects.get(id=kwargs['pk']).delete()
        return JsonResponse({'deleted': True})


class CreateBillsReceive(View):
    def post(self, request, *args, **kwargs):
        form = ContaReceberForm(request.POST or None)
        if form.is_valid():
            # form.cleaned_data["descricao"]
            print('form is valid')
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'created': 'True'})
        print('form not valid')
        return render(self.request, 'views_ajax/form_conta_pagar.html', {
            'form': form,
            'id_object': 0,
            'name_client': 'novo cliente',
        })


class UpdateBillsReceive(View):
    def post(self, *args, **kwargs):
        billspay = BillsReceive.objects.get(id=kwargs['pk'])
        form = ContaReceberForm(self.request.POST or None, self.request.FILES or None, instance=billspay)
        if form.is_valid():
            print('form is valid')
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        print('form not valid')
        return render(self.request, 'views_ajax/form_conta_pagar.html', {
            'form': form,
            'id_object': billspay.id,
            'name_client': billspay.nome_completo
        })


class DeleteBillsReceive(View):
    def post(self, *args, **kwargs):
        BillsReceive.objects.get(id=kwargs['pk']).delete()
        return JsonResponse({'deleted': True})