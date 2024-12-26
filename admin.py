from django.contrib import admin

# Register your models here.
# myapp/admin.py

from .models import Vendor, ProcurementHistory

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_type', 'contact_person', 'status')

@admin.register(ProcurementHistory)
class ProcurementHistoryAdmin(admin.ModelAdmin):
    list_display = ('purchase_order', 'vendor', 'amount', 'date', 'status')


