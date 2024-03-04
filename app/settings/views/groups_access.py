from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.views.generic import ListView

from ..forms import CreateGroupForm
from ...accounts.models import Collaborator

User = get_user_model()


class ListGroupsAccess(LoginRequiredMixin, ListView):
    model = Group
    fields = '__all__'
    template_name = 'views_ajax/groups/list_groups.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = self.get_queryset()
        return context


class CreateGroupAccess(LoginRequiredMixin, View):
    form_class = CreateGroupForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print(form)
        return render(request, 'views_ajax/groups/form_group.html',
                      {'form': form, 'pk': 0})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk', 0)
        print(request.POST.get('name', 'sem nome'))
        form = self.form_class(request.POST or None)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            form.save_m2m()
            return JsonResponse({'created': 'True'})
        else:
            print(form.errors)
            return render(request, 'views_ajax/groups/form_group.html',
                          {'form': form, 'pk': pk})


class ChangeGroupAccess(LoginRequiredMixin, View):
    form_class = CreateGroupForm

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs['pk'])
        print(group)
        form = self.form_class(instance=group)
        print(form)
        return render(request, 'views_ajax/groups/form_group.html',
                      {'form': form, 'pk': kwargs['pk']})

    def post(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs['pk'])
        form = self.form_class(request.POST or None, instance=group)
        if form.is_valid():
            print('valid')
            group = form.save()
            for user in Collaborator.objects.get_user_type('employee').filter(access_group=group):
                user.groups.clear()
                user.user_permissions.clear()
                print(group)
                user.groups.add(group)
                for permission in group.permissions.all():
                    user.user_permissions.add(permission)
            return JsonResponse({'updated': 'True',
                                 'user': group.name})
        else:
            print('not valid')
            print(form.errors)
            return render(request, 'views_ajax/groups/form_group.html', {'form': form, 'password_changed': False})


class DeleteGroupAccess(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs['pk'])
        return render(request, 'views_ajax/groups/delete_group.html',
                      {'pk': kwargs['pk'], 'name_object': group.name})

    def post(self, request, *args, **kwargs):
        Group.objects.get(id=kwargs['pk']).delete()
        return JsonResponse({'deleted': True})



