import logging
from typing import List
from django.db import models

logger = logging.getLogger(__name__)


class ClientManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def actives(self) -> List:
        return (
            self.get_queryset()
            .filter(
                is_active=True
            )
        )
