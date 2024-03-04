from django.urls import path
from .views import (
    DashboardView, NewVenda, ListaVendas, EditPedido,
    DeletePedido, filtra_produtos,
    )
from .views_ajax import (EditItem, ItemAdditionQTED,
                         ItemDecrementQTED, AddItemVenda,
                         DeleteItem, ListItensVenda, UpdateHeadVenda,
                         FormPagamentoView, AlterStatus, ListVendas, CardsMachines)

urlpatterns = [
    path('', ListaVendas.as_view(), name='lista-vendas'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('lista/', ListVendas.as_view(), name='vendas'),
    path('create/', NewVenda.as_view(), name="novo-pedido"),
    path('update/<int:venda>/', EditPedido.as_view(), name="edit-pedido"),
    path('delete/<int:venda>/', DeletePedido.as_view(), name="delete-pedido"),
    path('update-header/<int:pk>/', UpdateHeadVenda.as_view(), name="update_header"),
    path('alter-status/<int:venda>/', AlterStatus.as_view(), name="alterar"),

    path('items-venda/<int:id_venda>', ListItensVenda.as_view(), name="list_itens"),
    path('item-venda/add/<int:id_venda>/', AddItemVenda.as_view(), name='add_item_list'),
    path('item-venda/update/<int:item>/',  EditItem.as_view(), name='update_item'),
    path('item-venda/delete/<int:item>/', DeleteItem.as_view(), name="delete_item"),
    path('item-venda/decrement/<int:item>/', ItemDecrementQTED.as_view(), name="decrement_item"),
    path('item-venda/addition/<int:item>/', ItemAdditionQTED.as_view(), name="addition_item"),

    path('form_pagamento/<int:venda>/', FormPagamentoView.as_view(), name="form_pagamento"),
    path('form_pagamento/card_machines/<int:id_maq>/', CardsMachines.as_view(), name="get_card_machines"),
    path('form_pagamento/card_machines/', CardsMachines.card_machine, name='list_card_machines'),
    path('filtra-controle_contas/', filtra_produtos, name='filtra_produtos'),
]