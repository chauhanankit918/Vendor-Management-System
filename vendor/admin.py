from django.contrib import admin
from vendor.models import HistoricalPerformance, PurchaseOrder, Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'created_at',
        'updated_at')
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone_number')
    list_filter = ('gender', 'created_at')


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = (
        "po_number",
        "vendor",
        "order_date",
        "delivery_date",
        "items",
        "quantity",
        "status",
        "quality_rating",
        "issue_date",
        "acknowledgment_date",
        "created_at",
        "updated_at",
    )
    list_filter = ('order_date', 'delivery_date', 'issue_date', 'created_at')
    search_fields = ['po_number', 'vendor__first_name', 'vendor__last_name',]


class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "vendor",
        "date",
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
        "created_at",
        "updated_at",
    )
    list_filter = ('created_at',)
    search_fields = ['vendor__first_name', 'vendor__last_name',
                     'product__name']


admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
