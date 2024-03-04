from django.contrib import admin
from .models import Product,  Stock, Category


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'price')


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('product', 'current_stock', 'in_operation', 'minimum_stock')

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Category, CategoriaAdmin)
admin.site.register(Stock, EstoqueAdmin)
admin.site.register(Product, ProdutoAdmin)