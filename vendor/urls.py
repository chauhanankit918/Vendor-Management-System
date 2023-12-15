from rest_framework.routers import SimpleRouter

from vendor.apis import PurchaseOrderViewSet, VendorViewSet

router = SimpleRouter()
router.register(r'vendors',
                VendorViewSet,
                basename='vendors')
router.register(r'purchase_orders',
                PurchaseOrderViewSet,
                basename='purchase_orders')

urlpatterns = router.urls
