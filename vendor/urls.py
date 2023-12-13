from rest_framework.routers import SimpleRouter

from vendor.apis import VendorViewSet

router = SimpleRouter()
router.register(r'vendors-list',
                VendorViewSet,
                basename='vendors_list')

urlpatterns = router.urls
