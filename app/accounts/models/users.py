from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.utils.translation import gettext as _
from model_utils.fields import AutoCreatedField

from app.common.models import Base
from app.common.choices import TYPE_USER, PERMISSIONS
from app.companies.models import Company, UserCompany


from ..managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, Base):
    name = models.CharField(max_length=255, verbose_name=_('Nome'), null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, error_messages={'unique': 'Usuário com e-mail já existente.'})
    phone = models.CharField(max_length=255, verbose_name=_('Telefone'), blank=True, null=True)
    photo = models.ImageField(verbose_name=_('Foto'), upload_to="photo_perfil", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnail_perfil", verbose_name=_('perfil thumbnail'), blank=True,
                                  null=True)
    type = models.CharField(
        max_length=20, default="employee", choices=TYPE_USER
    )
    access_group = models.ForeignKey(Group, verbose_name=_('group'), blank=True, null=True,
                                     on_delete=models.SET_NULL, related_name='access_group_user')
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
        verbose_name='Acesso ao Dashboard?',
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        verbose_name='Ativo?',
    )
    ip = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP de Registro')
    agent = models.CharField(max_length=250, blank=True, null=True, verbose_name='Dispositivo')
    last_login = None

    objects = UserManager(type=["admin", "employee", "businessperson"])

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
        permissions = PERMISSIONS

    @property
    def company_id(self):
        company = UserCompany.objects.filter(user__id=self.pk).values('business__id').order_by('id').first() or {}
        return company.get('business__id') or None


class HistoryLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product_id = models.PositiveIntegerField(blank=True, null=True)
    company_id = models.PositiveIntegerField(blank=True, null=True)
    ip = models.GenericIPAddressField()
    agent = models.CharField(max_length=500)
    country = models.CharField(max_length=50, blank=True, null=True)
    created_at = AutoCreatedField(db_index=True, verbose_name=_('Criado em'))

    class Meta:
        verbose_name = 'Histórico de Login'
        verbose_name_plural = 'Históricos de Login'