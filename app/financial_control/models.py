from django.db import models
from app.common import choices
from django.contrib.auth import get_user_model
from app.common.models import Base
from .config_html import config_html, config_html_inputs, config_html_outputs

User = get_user_model()


class Movements(Base):
    type_mov = models.CharField(max_length=6, choices=choices.TYPE_MOVEMENT, verbose_name='TIPO')
    id_object = models.CharField(max_length=16, blank=True, null=True)
    movement = models.CharField(max_length=18, choices=choices.MOVEMENTS)
    detail_movement = models.CharField(max_length=35)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Vendendor')

    form_pg = models.CharField(max_length=50, choices=choices.FORMA_PG, verbose_name='Forma de pagamento')
    val_card = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    val_card_liq = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    val_pix = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    val_money = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    val_total = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    config_html = models.JSONField(default=dict, verbose_name="Dados do Movimento")

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

    def __str__(self) -> str:
        return str(self.id_movement) + ' - ' + self.movement

    def save(self, *args, **kwargs):
        if self.type_mov == 0:
            self.config_html = config_html['config_outputs']
        else:
            self.config_html = config_html['config_inputs']
        print(self.config_html)
        super().save(*args, **kwargs)

    @staticmethod
    def my_entries():
        entries = Movements.objects.filter(type_mov=1).aggregate(
            val_total=models.Sum('val_total'),
            val_pix=models.Sum('val_pix'),
            val_card=models.Sum('val_card'),
            val_card_liq=models.Sum('val_money'),
            val_money=models.Sum('val_money')
        )
        return {'val_total': entries['val_total'] or 0.00,
                'val_pix': entries['val_pix'] or 0.00,
                'val_card': entries['val_card'] or 0.00,
                'val_card_liq': entries['val_card_liq'] or 0.00,
                'val_money': entries['val_money'] or 0.00
                }

    @staticmethod
    def my_outings():
        return Movements.objects.filter(type_mov=0).aggregate(
            outings=models.Sum('val_total')
        )


class BillsReceive(Base):
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=5, choices=choices.CONTA_A_RECEBER, verbose_name='Categorias')
    status = models.CharField(max_length=50, default='not_received',
                              choices=choices.STATUS_PAYMENT_A_RECEBER, verbose_name='Status')

    class Meta:
        verbose_name = 'Conta a receber'
        verbose_name_plural = 'Contas a receber'
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.description


class BillsPay(Base):
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=5, choices=choices.CONTA_A_PAGAR, verbose_name='Categorias')
    status = models.CharField(max_length=50, default='not_pay',
                              choices=choices.STATUS_PAYMENT_A_PAGAR, verbose_name='Status')

    class Meta:
        verbose_name = 'Contas a Pagar/Receber'
        verbose_name_plural = 'Contas a Pagar/Receber'
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.description
