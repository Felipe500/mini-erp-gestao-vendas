from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

from django.contrib.auth import update_session_auth_hash, get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import CustomUserChangeForm

User = get_user_model()


class ChangeUserPerfil(LoginRequiredMixin, View):
    form_class = CustomUserChangeForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        form = CustomUserChangeForm(instance=user)
        photo_perfil = user.photo.url if user.photo else None
        return render(request, 'views_ajax/perfil_user/perfil_user.html',
                      {'form': form, 'photo_perfil': photo_perfil})

    def post(self, request, *args, **kwargs):
        set_user = User.objects.get(pk=request.user.pk)
        form = self.form_class(request.POST or None,  request.FILES or None, instance=set_user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return JsonResponse({'password_changed': 'True',
                                 'user': user.name})
        else:
            return render(request, 'views_ajax/perfil_user/perfil_user.html', {'form': form, 'password_changed': False})