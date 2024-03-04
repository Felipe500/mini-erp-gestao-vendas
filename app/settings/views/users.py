from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.accounts.models.collaborator import Collaborator
from ..forms import CreateUserForm, ChangeUserForm

User = get_user_model()


class ListUsers(LoginRequiredMixin, ListView):
    queryset = Collaborator.objects.get_user_type('employee')
    fields = '__all__'
    template_name = 'views_ajax/users/list_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = self.queryset.order_by('-created_at', '-updated_at')
        return context


class CreateUser(LoginRequiredMixin, View):
    form_class = CreateUserForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'views_ajax/users/create_user.html', {'form': form, 'pk': 0})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            print('valid')
            password = form.cleaned_data['password1']
            access_group = form.cleaned_data['access_group']
            form = form.save(commit=False)
            form.set_password(password)
            form.type = 'employee'
            form.save()

            form.groups.clear()
            form.user_permissions.clear()
            print(access_group)
            form.groups.add(access_group)
            for permission in form.access_group.permissions.all():
                form.user_permissions.add(permission)

            return JsonResponse({'created': 'True'})
        else:
            print('not valid')
            print(form.errors)
            return render(request, 'views_ajax/users/create_user.html',
                          {'form': form, 'pk': 0})


class ActiveUser(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = Collaborator.objects.get(pk=kwargs['pk'])
        user.is_active = not user.is_active
        user.save()
        return JsonResponse({'updated': 'True', 'user': user.name})


class ChangeUser(LoginRequiredMixin, View):
    form_class = ChangeUserForm

    def get(self, request, *args, **kwargs):
        user = Collaborator.objects.get(pk=kwargs['pk'])
        form = self.form_class(instance=user)
        return render(request, 'views_ajax/users/create_user.html',
                      {'form': form, 'pk': kwargs['pk']})

    def post(self, request, *args, **kwargs):
        user = Collaborator.objects.get(pk=kwargs['pk'])
        form = self.form_class(request.POST or None, instance=user)
        if form.is_valid():
            print('v')
            form = form.save(commit=False)
            form.save()

            form.groups.clear()
            form.user_permissions.clear()

            form.groups.add(form.access_group)
            for permission in form.access_group.permissions.all():
                form.user_permissions.add(permission)

            return JsonResponse({'updated': 'True',
                                 'user': form.name})
        else:
            print(form.errors)
            return render(request, 'views_ajax/users/create_user.html',
                          {'form': form, 'password_changed': False, 'pk': kwargs['pk']})


class DeleteUser(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Collaborator.objects.get(pk=kwargs['pk'])
        return render(request, 'views_ajax/users/delete_user.html',
                      {'pk': kwargs['pk'], 'name_object': user.name})

    def post(self, request, *args, **kwargs):
        Collaborator.objects.get_collaborator().filter(id=kwargs['pk']).delete()
        return JsonResponse({'deleted': True})