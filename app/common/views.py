from django.http import JsonResponse, HttpResponseForbidden
from django.views import View

from django.shortcuts import render

from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.accounts.models.collaborator import Collaborator


User = get_user_model()

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin


class MyView(PermissionRequiredMixin, View):
    template = 'not_authorized.html'
    permission_required = 'myapp.change_item'

    def handle_no_permission(self):
        messages.error(self.request, 'You dont have permission to do this')
        return super(MyView, self).handle_no_permission()


class MixListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    def dispatch(self, request, *args, **kwargs):
        print(self.request.user.get_all_permissions())
        if not self.request.user.has_perm(self.permission_required):
            print('not permissao')
            return render(self.request, '403.html', status='403')
        return super().dispatch(request, *args, **kwargs)


class MixView(LoginRequiredMixin, View):
    permission_required = None

    def dispatch(self, request, *args, **kwargs):
        print(self.request.user.get_all_permissions())
        if not self.request.user.has_perm(self.permission_required):
            print('not permissao')
            return render(self.request, '403.html', status='403')
        return super().dispatch(request, *args, **kwargs)
