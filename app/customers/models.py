from django.utils.translation import gettext_lazy as _
from django.db import models

from app.customers.managers import ClientManager
from app.common.models import Base
from django.contrib.auth import get_user_model

User_funcionario = get_user_model()


class Customer(Base):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50,null=True, blank=True)
    seller = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.CASCADE)

    is_active = models.BooleanField(verbose_name=_('Ativo?'), default=True)

    objects = ClientManager()

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
        ordering = ['name', '-created_at']

    @property
    def nome_completo(self):
        if self.surname:
            return self.name + ' ' + self.surname
        return self.name + ' '

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        if self.surname:
            return self.name + ' ' + self.surname
        return self.name + ' '






