import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# The rest of your script

from myapp.models import Vendor, ProcurementHistory

def run():
    # Create Vendor
    vendor = Vendor.objects.create(
        name="XYZ Enterprises",
        business_type="Manufacturing",
        contact_person="Jane Smith",
        phone_number="9876543210",
        email="xyz@enterprises.com",
        address="456 Secondary St, City, Country",
        status="Inactive"
    )

    # Add Procurement History
    ProcurementHistory.objects.create(
        vendor=vendor,
        purchase_order="PO456",
        amount=500.00,
        date="2024-12-21",
        status="Pending"
    )

    print("Sample data added successfully!")
