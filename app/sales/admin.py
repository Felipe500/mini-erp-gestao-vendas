from django.contrib import admin
from .models import Sale, ItemsSale
from .actions import nfe_emitida, nfe_nao_emitida


class ItemsSaleInline(admin.TabularInline):
    model = ItemsSale
    extra = 1


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'seller', 'value', 'status', 'created_at')
    readonly_fields = ('value', 'total_discount')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [ItemsSaleInline]

    def total(self, obj):
        return obj.get_total()
    total.short_description = 'Total'


admin.site.register(Sale, SaleAdmin)
admin.site.register(ItemsSale)
