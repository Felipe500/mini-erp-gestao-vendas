from django.db import models
from django.utils import timezone

from app.common.models import Base


class UserCompany(models.Model):
    business = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False, verbose_name='Bloqueado ?')
    created_at = models.DateTimeField(editable=False, blank=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies_company_users'
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return f"{self.business} | {self.user}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Company(Base):
    business_name = models.CharField(max_length=100)
    document = models.CharField(max_length=130, blank=True, null=True, verbose_name='CNPJ')
    users = models.ManyToManyField('accounts.User', through='UserCompany', related_name='users_in_company')
    zipcode = models.CharField(max_length=40, blank=True, null=True, verbose_name='Cep')
    uf = models.CharField(max_length=2, blank=True, null=True, verbose_name='Estado')
    city = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cidade')
    district = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Número')
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name='Endereço')
    complement = models.CharField(max_length=250, blank=True, null=True, verbose_name='Complemento')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
