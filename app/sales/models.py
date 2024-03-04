from django.db import models
from django.db.models.signals import post_save,  post_delete
from django.db.models import Sum, F, DecimalField
from django.dispatch import receiver
from app.customers.models import Customer
from app.products.models import Product
from django.utils.translation import gettext as _
from .managers import VendaManager
from django.contrib.auth import get_user_model
from app.common.models import TimeStampedModel, Base
from decimal import Decimal
from app.common.choices import STATUS_SALE

User = get_user_model()


class Sale(Base):
    value = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name=_('valor'))
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name=_('desconto'))
    total_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name=_('valor total em desconto'))
    client = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('cliente'))
    seller = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('vendendor'))
    status = models.CharField(choices=STATUS_SALE, default=STATUS_SALE.not_pay, max_length=7, verbose_name=_('status'))
    is_canceled = models.BooleanField(default=False, verbose_name=_('venda cancelada'))

    statistic = VendaManager()

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.pk}"

    def calculate_total(self):
        total = self.itemssale_set.all().aggregate(
            tot_ped=Sum((F('quantity') * F('product__price')) - F('discount'), output_field=DecimalField())
        )['tot_ped'] or 0
        total_discount = self.itemssale_set.all().aggregate(Sum('discount'))['discount__sum'] or 0
        total = total - Decimal(self.discount)
        Sale.objects.filter(id=self.id).update(value=total, total_discount=(total_discount + self.discount))
        return total

    def replenishment_for_stock(self):
        items = self.itemssale_set.all()
        for item in items:
            print(item.quantity)

    def __str__(self):
        return str(self.pk) + '- venda'


class ItemsSale(TimeStampedModel):
    qted_prev = 0
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name=_('Venda'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('produto'))
    quantity = models.IntegerField(verbose_name=_('quantidade'))
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('desconto'))

    class Meta:
        verbose_name_plural = "Itens do pedido"
        unique_together = [['sale', 'product']]

    def save(self, *args, **kwargs):
        super(ItemsSale, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.sale) + ' - ' + self.product.description


@receiver(post_delete, sender=ItemsSale)
def update_items_sale(sender, instance, **kwargs):
    instance.sale.calculate_total()


@receiver(post_delete, sender=Sale)
def alter_stock(sender, instance, **kwargs):
    instance.replenishment_for_stock()


@receiver(post_save, sender=Sale)
def update_sale(sender, instance, **kwargs):
    instance.calculate_total()
