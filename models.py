from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name





class Vendor(models.Model):
    name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ])
    
    def __str__(self):
        return self.name


class ProcurementHistory(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='procurement_history')
    purchase_order = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Completed', 'Completed'), ('Pending', 'Pending')])

    def __str__(self):
        return f"{self.purchase_order} - {self.vendor.name}"


class PurchaseOrder(models.Model):
    vendor_id = models.IntegerField()
    item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} for Vendor {self.vendor_id}"



class Payment(models.Model):
    status = models.CharField(max_length=50)  # Example field for payment status
    date = models.DateField()  # Example field for payment date
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Example field for payment amount

    def __str__(self):
        return f"Payment of {self.amount} on {self.date}"


# myapp/models.py




