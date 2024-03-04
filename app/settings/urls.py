from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from .views import (SettingsPageInicial, ChangeUserPerfil, ChangePassword, CreateMachineCard, ListMachineCard,
                    ChangeMachineCard,  DeleteMachineCard, ListUsers, CreateUser, ActiveUser, ChangeUser, DeleteUser,
                    ListGroupsAccess, CreateGroupAccess, ChangeGroupAccess, DeleteGroupAccess
                    )


urlpatterns = [
    path('', SettingsPageInicial.as_view(), name="settings_app"),
    path('create_new_maq', CreateMachineCard.as_view(), name="create_new_maq"),

    path('alter-password/', ChangePassword.as_view(), name="change-password"),
    path('change-perfil_user/', ChangeUserPerfil.as_view(), name="alterar_user_perfil"),

    path('payments/machine-card/', ListMachineCard.as_view(), name="lista_maq_cartao"),
    path('payments/machine-card/create/', CreateMachineCard.as_view(), name="criar_maq_cartao"),
    path('payments/machine-card/update/<int:pk>/', ChangeMachineCard.as_view(), name="atualizar_maq_cartao"),
    path('payments/machine-card/delete/<int:pk>/', DeleteMachineCard.as_view(), name="deletar_maq_cartao"),

    path('control_access/users', ListUsers.as_view(), name="list_users"),
    path('control_access/users/<int:pk>', ChangeUser.as_view(), name="get_user"),
    path('control_access/users/create_user', CreateUser.as_view(), name="create_user"),
    path('control_access/users/delete/<int:pk>', DeleteUser.as_view(), name="create_user"),
    path('control_access/users/active/<int:pk>', ActiveUser.as_view(), name="user_active"),

    path('control_access/groups', ListGroupsAccess.as_view(), name="list_groups"),
    path('control_access/groups/<int:pk>', ChangeGroupAccess.as_view(), name="get_group"),
    path('control_access/groups/create_group', CreateGroupAccess.as_view(), name="create_group"),
    path('control_access/groups/delete/<int:pk>', DeleteGroupAccess.as_view(), name="get_group"),


    path('update_maq/<int:id>/', PasswordChangeView.as_view(), name="update_maquina")
]