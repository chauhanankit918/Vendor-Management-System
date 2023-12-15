from rest_framework import mixins, viewsets
from vendor.models import PurchaseOrder, Vendor
from vendor.serializer import PurchaseOrderSerializer, VendorSerializer
from rest_framework.permissions import IsAuthenticated


class VendorViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    lookup_field = 'vendor_id'
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.data.get('vendor_code') is None:
            last_vendor = Vendor.objects.last()
            if last_vendor:
                request.data['vendor_code'] = last_vendor.id + 1
            else:
                request.data['vendor_code'] = 1
        return super().create(request, *args, **kwargs)


class PurchaseOrderViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    lookup_field = 'po_id'
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
