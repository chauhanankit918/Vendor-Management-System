from django.dispatch import receiver
from django.db.models.signals import post_save

from vendor.models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def post_update_historical_performance_save(
        sender, instance, created, **kwargs):
    old_obj = PurchaseOrder.objects.filter(
        vendor=instance.vendor).last()
    if instance.status == 'completed':
        old_obj = PurchaseOrder.objects.filter(
            vendor=instance.vendor).last()
        print(old_obj)

    print("*************")
