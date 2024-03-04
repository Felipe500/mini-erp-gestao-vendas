from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..models import MachineCard
from ..forms import FormMaq_cartao2


class ListMachineCard(LoginRequiredMixin, ListView):
    model = MachineCard
    fields = '__all__'
    template_name = 'views_ajax/payments/payments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_maq_card'] = self.get_queryset()
        return context


class CreateMachineCard(LoginRequiredMixin, View):
    form_class = FormMaq_cartao2

    def get(self, request, *args, **kwargs):
        form = FormMaq_cartao2()
        return render(request, 'views_ajax/payments/form_machine_card.html', {'form': form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'created': 'True'})
        else:
            print(form.errors)
            print(form.clean())
            return render(request, 'views_ajax/payments/form_machine_card.html', {'form': form})


class ChangeMachineCard(LoginRequiredMixin, View):
    form_class = FormMaq_cartao2

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        maq = MachineCard.objects.get(pk=pk)
        form = FormMaq_cartao2(instance=maq)
        return render(request, 'views_ajax/payments/form_machine_card.html', {'form': form,
                                                                         'pk': pk})

    def post(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        maq = MachineCard.objects.get(pk=pk)
        print(maq)
        form = self.form_class(request.POST or None, instance=maq)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        else:
            print(form.errors)
            return render(request, 'views_ajax/payments/form_machine_card.html', {'form': form,
                                                                             'pk': pk})


class DeleteMachineCard(LoginRequiredMixin, View):
    form_class = FormMaq_cartao2

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        maq = MachineCard.objects.get(pk=pk)
        print(maq)
        return render(request, 'views_ajax/payments/delete_machine_card.html', {'pk': pk,
                                                                                'name_object': maq.nome})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        MachineCard.objects.get(id=kwargs['pk']).delete()
        return JsonResponse({'deleted': True})
