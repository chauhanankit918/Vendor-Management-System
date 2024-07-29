from django.contrib import admin
from django.urls import path, include
from vendor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('api/', include('vendor.urls')),
    path('create_order/', views.create_order, name='create_order'),
    path('payment/success/', views.payment_success, name='payment_success'),
]
