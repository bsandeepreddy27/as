from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

    def save(self, *args, **kwargs):
        # Automatically calculate total_price before saving
        self.total_price = self.quantity * self.unit_price
        super(PurchaseOrder, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.order_number} - {self.item}"
    
class ProcurementRequest(models.Model):
    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    request_id = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item_details = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES)
    status = models.CharField(max_length=50, default="Pending")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request #{self.request_id} - {self.item_details}"

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    procurement_request = models.ForeignKey('ProcurementRequest', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Payment {self.id} - {self.status}"


class Payment(models.Model):
    invoice_id = models.CharField(max_length=20)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    due_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def get_status_display(self):
        return self.get_status_display()

    def __str__(self):
        return self.invoice_id 
       
class Report(models.Model):
    # Define the fields for the Report model
    report_type = models.CharField(max_length=100)

    def generate_report(self):
        # Ensure proper indentation inside the function
        if self.report_type == 'procurement':
            # Your logic for generating the report goes here
            pass
