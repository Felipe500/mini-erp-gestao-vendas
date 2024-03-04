from django.db import models
from django.db.models import Max, Avg, Min, Count


class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('value'))['value__avg'] or 0

    def media_desconto(self):

        return self.all().aggregate(Avg('discount'))['discount__avg'] or 0

    def min(self):
        return self.all().aggregate(Min('value'))['value__min'] or 0

    def max(self):
        return self.all().aggregate(Max('value'))['value__max'] or 0

    def num_pedidos(self):
        return self.all().aggregate(Count('id'))['id__count'] or 0