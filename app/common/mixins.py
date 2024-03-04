from django.http import JsonResponse


class CheckPermissions():

    def dispatch(self, request, *args, **kwargs):
        print(self.has_permission())
        if not self.has_permission():
            return JsonResponse({'not_allowed': 'True'})
        return super().dispatch(request, *args, **kwargs)
