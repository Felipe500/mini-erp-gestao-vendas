from django.db.models.signals import post_save
from .models import Stock, Product
from django.dispatch import receiver


@receiver(post_save, sender=Product)
def update_count_lessons_current_course(sender, instance, created, **kwargs):
    if created:
        pass

