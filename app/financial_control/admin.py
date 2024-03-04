from django.contrib import admin
from .models import BillsPay, BillsReceive, Movements


@admin.register(Movements)
class MovementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_mov', 'id_object', 'movement', 'form_pg', 'val_card', 'val_pix', 'val_money', 'val_total']


@admin.register(BillsPay)
class ContaPagarAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'category', 'value', 'status']


@admin.register(BillsReceive)
class ContaReceberAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'category', 'value', 'status']