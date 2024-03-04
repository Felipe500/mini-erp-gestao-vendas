from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render


class CustomPermissionRequire(AccessMixin):
    permission_required = None
    template_denied = None

    def get_permission_required(self):
        if self.permission_required is None:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} is missing the "
                f"permission_required attribute. Define "
                f"{self.__class__.__name__}.permission_required, or override "
                f"{self.__class__.__name__}.get_permission_required()."
            )
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    def has_permission(self):
        """
        Override this method to customize the way permissions are checked.
        """
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms)

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return render(request, '403.html', status='403')
        return super().dispatch(request, *args, **kwargs)
