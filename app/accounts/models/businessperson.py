from django.contrib.auth.hashers import make_password

from app.common.choices import TYPE_USER
from app.common import utils
from ..models import User
from ..managers import UserManager


class Businessperson(User):
    objects = UserManager(type=['businessperson'])

    class Meta:
        proxy = True
        verbose_name = 'Empresário'
        verbose_name_plural = 'Empresários'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = TYPE_USER.producer
            self.is_superuser = False
            self.is_staff = False

        if not self.password:
            self.password = make_password(utils.random_password(20))

        super().save(*args, **kwargs)


