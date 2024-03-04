from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core import serializers
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView
from django.views import View

from app.common.hash_permissions import CustomPermissionRequire

from .models import Customer
from .forms import ClienteReadOnlyForm, ClienteForm
from app.common.views import MixView, MixListView


class ViewClient(MixView):
    def get(self, request, id):
        cliente = Customer.objects.get(id=id)
        form = ClienteReadOnlyForm(instance=cliente)
        return render(request, 'views_ajax/form_client.html', {'form': form})


class ViewCreateClient(MixView):
    def get(self, *args, **kwargs):
        form = ClienteForm()
        return render(self.request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': 0,
            'name_client': 'Cliente Novo'
        })

    def post(self,  *args, **kwargs):
        form = ClienteForm(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'created': 'True'})
        print(form.errors)
        return render(self.request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': 0,
            'name_client': 'novo cliente',
        })


class ViewUpdateClient(MixView):
    def get(self, request, id):
        cliente = Customer.objects.get(id=id)
        form = ClienteForm(instance=cliente)
        return render(request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': cliente.id,
            'name_client': cliente.nome_completo
        })

    def post(self,  *args, **kwargs):
        cliente = Customer.objects.get(id=kwargs['id'])
        print(cliente.birth_date)
        form = ClienteForm(self.request.POST or None, self.request.FILES or None, instance=cliente)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'updated': 'True'})
        print(form.errors)
        return render(self.request, 'views_ajax/form_client.html', {
            'form': form,
            'id_client': cliente.id,
            'name_client': cliente.nome_completo
        })


class ViewDeleteClient(MixView):
    permission_required = 'accounts.app_clients'

    def get(self, request, id):
        cliente = Customer.objects.get(id=id)
        form = ClienteReadOnlyForm(instance=cliente)
        return render(request, 'views_ajax/client_delete.html', {
            'form': form,
            'id_client': cliente.id,
            'name_client': cliente.nome_completo,
        })

    def post(self,  *args, **kwargs):
        Customer.objects.get(id=kwargs['id']).delete()
        return JsonResponse({'deleted': True})


class PersonListAjax(MixListView):
    paginate_by = 2
    model = Customer
    fields = '__all__'
    template_name = 'views_ajax/get_list_clients.html'
    form_filter = None
    permission_required = 'accounts.app_clients_view'

    def dispatch(self, request, *args, **kwargs):
        print(self.has_permission())
        if not self.has_permission():
            return JsonResponse({'status':'403','message':'Acesso Não Autorizado'}, status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return self.model.objects.filter(
                Q(name__unaccent__icontains=query) | Q(surname__unaccent__icontains=query)
            )
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['clientes'] = paginator.page(page)
        return context


def filter_clients(request):
    query = request.GET.get('query', None)
    if query:
        queryset = Customer.objects.filter(
            Q(name__unaccent__icontains=query) | Q(surname__unaccent__icontains=query)
        )
        qs_json = serializers.serialize('json', queryset)
        print(qs_json)
        return JsonResponse(qs_json)
    else:
        return JsonResponse(serializers.serialize('json', Customer.objects.all()), content_type='application/json')

