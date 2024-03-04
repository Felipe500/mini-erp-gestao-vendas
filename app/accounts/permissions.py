from rest_framework import permissions

from django.conf import settings


class ProducerPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == "producer"


class AdminPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == "admin"


class BTokenPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.headers.get('Btoken') == settings.BTOKEN
