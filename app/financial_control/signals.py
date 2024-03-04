from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BillsPay, BillsReceive, Movements


@receiver(post_save, sender=BillsPay)
def save_bills_pay(sender, instance, created, **kwargs):
    if instance.status == 'pay':
        if Movements.objects.all_objects(id_object=instance.id, movement='account_paid').exists():
            Movements.objects.filter(id_object=instance.id, movement='account_paid').update(deleted_at=None)
        else:
            Movements.objects.create(**{
                'type': 0,
                'id_object': instance.id,
                'movement': 'account_paid',
                'val_total': instance.value,
                'val_money': instance.value,
            })


@receiver(post_save, sender=BillsReceive)
def save_bills_receive(sender, instance, created, **kwargs):
    if instance.status == 'pay':
        if Movements.all_objects.filter(id_object=instance.id, movement='account_received').exists():
            Movements.all_objects.filter(id_object=instance.id, movement='account_received').update(deleted_at=None)
        else:
            Movements.objects.create(**{
                'type': 1,
                'id_object': instance.id,
                'movement': 'account_received',
                'val_total': instance.value,
                'val_money': instance.value,
            })
