from ..models import User
from ..managers import UserManager

from app.common.choices import TYPE_USER


class Collaborator(User):
    objects = UserManager(type=[TYPE_USER.employee])

    class Meta:
        proxy = True
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = TYPE_USER.employee
            self.is_superuser = False
            self.is_staff = False
        super().save(*args, **kwargs)