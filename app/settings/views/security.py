from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render

from django.contrib.auth import update_session_auth_hash, get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ..forms import PasswordChangingForm

User = get_user_model()


class ChangePassword(LoginRequiredMixin, TemplateView):
    success_url = reverse_lazy('password_success')
    form_class = PasswordChangingForm

    def get(self, request, *args, **kwargs):
        form_class = PasswordChangingForm
        form = PasswordChangingForm(self.request.user)
        return render(request, 'views_ajax/security/change_password.html',{'form': form,})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return JsonResponse({'password_changed': 'True'})
        else:
            return render(request, 'views_ajax/security/change_password.html', {'form': form, 'password_changed': False})