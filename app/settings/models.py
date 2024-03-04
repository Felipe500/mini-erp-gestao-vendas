from django.db import models
from app.common.models import Base


class MachineCard(Base):
    name = models.CharField(max_length=40, blank=True)
    deb = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre5 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre6 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre7 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre8 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre9 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre10 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre11 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cre12 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Máquina de cartão'
        verbose_name_plural = 'Máquinas de cartão'

    def __str__(self):
        return self.name

    def json_export(self):
        data = {'deb': self.deb, 'cre1': self.cre1, 'cre2': self.cre2, 'cre3': self.cre3, 'cre4': self.cre4,
                'cre5': self.cre5, 'cre6': self.cre6, 'cre7': self.cre7, 'cre8': self.cre8, 'cre9': self.cre9,
                'cre10': self.cre10, 'cre11': self.cre11, 'cre12': self.cre12}
        return data
