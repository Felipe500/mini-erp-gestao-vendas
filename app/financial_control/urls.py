from django.urls import include
from .views import *
from .views_ajax import *
from .actions_ajax import *


from django.urls import path
from .views import MovementsView, NovaEntrada
from .views_ajax import ListMovements


urlpatterns = [


]

urlpatterns = [
    path('minhas-movimentacoes', MovementsView.as_view(), name="movimentacoes"),
    path('nova-entrada', NovaEntrada.as_view(), name="nova_entrada"),
    path('lista_movimentacoes/', ListMovements.as_view(), name="lista_movimentacoes"),

    path('a-receber/', include([
        path('', ContaReceberListView.as_view(), name="contas_receber"),

        # views ajax
        path('list/', ListToReceive.as_view(), name="list_contas_receber"),
        path('view_nova_conta/', ViewCreateBillsReceive.as_view(), name="view_nova_conta_2"),
        path('view_atualizar/<int:pk>/', ViewUpdateBillsReceive.as_view(), name="view_atualizar"),
        path('view_deletar/<int:pk>/', ViewDeleteBillsReceive.as_view(), name="view_deletar"),

        # actions ajax
        path('criar/', CreateBillsReceive.as_view(), name="nova_conta_receber"),
        path('atualizar/<int:pk>/', UpdateBillsReceive.as_view(), name="atualizar_conta_receber"),
        path('deletar/<int:pk>/', DeleteBillsReceive.as_view(), name="deletar_conta_receber"),
    ])),

    path('a-pagar/', include([
        path('', ContaPagarListView.as_view(), name="contas_pagar"),
        path('list/', ListBillsPay.as_view(), name="list_contas_pagar"),

        # actions ajax
        path('criar/', CreateBillsPay2.as_view(), name="nova_conta"),
        path('atualizar/<int:pk>/', ChangeBillsPay2.as_view(), name="atualizar_conta"),
        path('deletar/<int:pk>/', DeleteBillsPay2.as_view(), name="atualizar_conta"),
    ])),
]