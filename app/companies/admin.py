from django.contrib import admin
from .models import Company, UserCompany


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ('business_name',)
    list_filter = ['users', 'document']
    list_display = ['id', 'business_name']


@admin.register(UserCompany)
class UserCompanyAdmin(admin.ModelAdmin):
    search_fields = ('business',)
    list_filter = ['user', 'is_blocked']
    list_display = ['business', 'is_blocked']
