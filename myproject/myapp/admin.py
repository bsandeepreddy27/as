from django.contrib import admin
from .models import Vendor, PurchaseOrder

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'contact_email', 'contact_phone')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'vendor', 'item', 'quantity', 'unit_price', 'total_price', 'status', 'date_created')
    list_filter = ('status', 'vendor', 'date_created')
    search_fields = ('order_number', 'item', 'vendor__name')
