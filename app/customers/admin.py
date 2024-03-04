from django.contrib import admin
from .models import Customer


class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('name', 'surname', 'email', 'phone', 'birth_date', 'is_active')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('address', 'zip', 'seller')
        })
    )
    list_display = ('name', 'surname', 'email', 'phone')
    search_fields = ('name', 'surname')


admin.site.register(Customer, ClienteAdmin)
