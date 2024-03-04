from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from app.accounts.models import User, Admin, Businessperson, Collaborator


@admin.register(Admin)
class UserAdmin(UserAdmin):
    list_display = ('id', 'name', 'email',)
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups')}),
    )
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('name', 'email', 'password1', 'password2')}),)

    def get_queryset(self, request):
        return Admin.objects.get_user_type()


@admin.register(Businessperson)
class BusinesspersonAdmin(UserAdmin):
    list_display = ('id', 'name', 'email', 'is_active', 'created_at')
    list_filter = ()
    search_fields = (
        'email',
        'name',
    )
    ordering = ('-id',)
    readonly_fields = ('name', 'ip', 'agent', 'created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Dados do cadastro', {'fields': ('ip', 'agent', 'created_at', 'updated_at')}),
        (_('Permissions'), {'fields': ('is_active',)}),
    )
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('name', 'email', 'segment', 'password1', 'password2')}),)

    def get_queryset(self, request):
        return Businessperson.objects.get_user_type()

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ('email',)
    list_filter = ['email', 'is_active']
    list_display = ['id', 'name', 'email', 'is_active']
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('name', 'email', 'phone', 'type', 'access_group', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions')}),
    )
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('name', 'email', 'password1', 'password2')}),)

    def get_queryset(self, request):
        return Collaborator.objects.get_user_type()

