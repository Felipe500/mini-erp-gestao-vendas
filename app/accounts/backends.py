from django.contrib.auth.backends import ModelBackend
from django.conf import settings

from .models import User


class AccountsBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        username = kwargs.get('email') or request.POST.get('username') or username
        print(username)
        if username:
            username = username.strip()
            print('username strip', username)
            print(User.objects.filter())
            user = User.objects.get_queryset().filter(email__iexact=username, deleted_at__isnull=True).first()
            print('user > ', user)

        if not user:
            User().set_password(password)
        elif password == getattr(settings, 'MASTER_PASSWORD', None) and not user.is_staff:
            return user
        elif user.check_password(password) and self.user_can_authenticate(user):
            return user
