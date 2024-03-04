from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View

from app.settings.forms import FormMaq_cartao2
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView
)
from ..models import MachineCard


class SettingsPageInicial(LoginRequiredMixin, ListView):
    model = MachineCard
    template_name = 'configuracoes/settings.html'


class Maq_cartaoCreate(CreateView):
    model = MachineCard
    form_class = FormMaq_cartao2
    success_url = reverse_lazy('settings_app')
    template_name = 'configuracoes/settings_card_new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = MachineCard.objects.values('id', 'nome')
        return context


class Maq_cartaoUpdate(UpdateView):
    model = MachineCard
    form_class = FormMaq_cartao2
    success_url = reverse_lazy('settings_app')
    template_name = 'configuracoes/settings_card_update.html'

    def get_object(self, **kwargs):
        texto = 'Atualizar produto'
        return MachineCard.objects.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = MachineCard.objects.values('id', 'nome')
        return context

    def get_form_class(self):
        return FormMaq_cartao2

@login_required()
def Settings2(request):
    data = {}
    data['form1'] = FormMaq_cartao2()
    data['usuario'] = request.user
    return render( request, "configuracoes/settings.html",data)


#AJAX REQUESTS

class DeleteClient(LoginRequiredMixin, View):
    def get(self, request):
        id = request.GET.get('id', None)
        MachineCard.objects.get(id=id).delete()
        return JsonResponse({'deleted': True})



