from django.contrib import admin
from vendor.models import (AuthToken,
                           HistoricalPerformance,
                           PurchaseOrder,
                           Vendor)
from django.contrib.auth.admin import UserAdmin


class CustomVendorAdmin(UserAdmin):
    model = Vendor
    list_display = (
        'pk',
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

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name', 'vendor_code', 'gender',
                'place_of_birth', 'datetime_of_birth', 'address', 'city',
                'country_of_origin', 'on_time_delivery_rate',
                'quality_rating_avg', 'average_response_time',
                'fulfillment_rate'
            )
        }),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',
                                    'user_permissions')}),
        ('Group Permissions', {'fields': ('groups', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


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


class AuthTokenAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "key",
    )
    search_fields = ['user__first_name', 'user__last_name', 'key']


admin.site.register(Vendor, CustomVendorAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
admin.site.register(AuthToken, AuthTokenAdmin)
