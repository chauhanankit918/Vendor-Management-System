from rest_framework import serializers
from vendor.models import PurchaseOrder, Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            'first_name', 'last_name', 'vendor_code', 'gender',
            'place_of_birth', 'datetime_of_birth', 'address', 'city',
            'country_of_origin', 'on_time_delivery_rate',
            'quality_rating_avg', 'average_response_time',
            'fulfillment_rate')


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
