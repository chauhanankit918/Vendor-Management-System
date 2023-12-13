from rest_framework import mixins, viewsets
from vendor.models import Vendor
from vendor.serializer import VendorSerializer
# from rest_framework.permissions import IsAuthenticated


class VendorViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    lookup_field = 'vendor_id'
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
