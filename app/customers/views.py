from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Customer
from .filters import ClienteFilter


class ClientList(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Customer
    fields = '__all__'
    template_name = 'client.html'
    form_filter = None
    permission_required = 'accounts.app_clients_view'

    def dispatch(self, request, *args, **kwargs):
        print(self.request.user.get_all_permissions())
        if not self.request.user.has_perm(self.permission_required):
            print('not permissao')
            return render(self.request, '403.html', status='403')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.form_filter = ClienteFilter(self.request.GET, queryset=self.queryset)
        return self.form_filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['form_filter'] = ClienteFilter(self.request.GET, queryset=self.queryset)
        context['clientes'] = paginator.page(page)
        return context


class PersonList2(LoginRequiredMixin, ListView):
    model = Customer

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo ao seu primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Voce ja acessou hoje'

        return context



