from django.db import models
from django.utils.translation import ugettext_lazy as _


class Vendor(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = "m", _("Male")
        FEMALE = "f", _("Female")
        OTHER = "o", _("Other")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    vendor_code = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=1,
                              choices=GenderChoice.choices,
                              default=GenderChoice.MALE)
    place_of_birth = models.CharField(max_length=255, blank=True)
    datetime_of_birth = models.DateTimeField(null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=255, null=True, blank=True)
    country_of_origin = models.CharField(
        max_length=50, blank=True, default="IN", null=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=255, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=255)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
