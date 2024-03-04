from typing import List
from django.db import models


class CategoriaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def actives(self) -> List:
        return (
            self.get_queryset()
            .filter(
                is_active=True
            )
        )


class ProdutoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def actives(self) -> List:
        return (
            self.get_queryset()
            .filter(
                is_active=True
            )
        )


class EstoqueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def actives(self) -> List:
        return (
            self.get_queryset()
            .filter(
                is_active=True
            )
        )