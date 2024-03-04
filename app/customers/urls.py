from django.urls import path
from .views import ClientList
from .view_ajax import (PersonListAjax, ViewClient,
                        ViewCreateClient, ViewDeleteClient, ViewUpdateClient,
                        filter_clients)


urlpatterns = [
    path('', ClientList.as_view(), name="client_list"),
    # ajax actions
    path('create/', ViewCreateClient.as_view(), name='crud_ajax_create'),
    path('delete/<int:id>/',  ViewDeleteClient.as_view(), name='crud_ajax_delete'),
    path('update/<int:id>/', ViewUpdateClient.as_view(), name='crud_ajax_update'),
    path('list_client/',  PersonListAjax.as_view(), name='crud_ajax_list'),
    # views
    path('view_client/<int:id>/',  ViewClient.as_view(), name='view_client'),
    path('list_clients/', filter_clients, name="select_clients"),

]