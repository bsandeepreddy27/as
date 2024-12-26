
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Vendor
from .models import PurchaseOrder  # Assuming you have a PurchaseOrder model
from django.http import JsonResponse

from .models import Payment


from django.contrib.auth.models import User

from django.contrib.auth import login
from django.contrib import messages


from django.contrib.auth import authenticate, login


# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login_user(request):
    if request.method == 'POST':  # Handle form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Authenticate user
        if user is not None:  # User exists
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to dashboard or another page
        else:
            messages.error(request, 'Invalid username/email or password.')  # Error message for invalid credentials
    return render(request, 'login.html')  # Render the login page for GET request


def signup(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return render(request, 'signup.html')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists. Please use a different email.")
            return render(request, 'signup.html')

        # Create the user if validations pass
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name  # Save the name
        user.save()

        # Automatically log in the user and redirect
        login(request, user)
        messages.success(request, "Signup successful! Welcome to the platform.")
        return redirect('dashboard')  # Adjust to your homepage or dashboard URL

    return render(request, 'signup.html')

def logout_user(request):
    return render(request, 'logout.html')

def profile(request):
    return render(request, 'profile.html')

def vendor_list(request):
    return render(request, 'vendor.html')

def vendor_details(request, id):
    return render(request, 'vendor-details.html')

def payment_list(request):
    return render(request, 'payments.html')

def payment_details(request, id):
    return render(request, 'payment-details.html')

def initiate_payment(request):
    if request.method == "POST":
        # Logic for processing payment
        invoice_id = request.POST.get('invoiceId')
        vendor_name = request.POST.get('vendorName')
        amount = request.POST.get('amount')
        payment_date = request.POST.get('paymentDate')
        # Process payment here...

        # Return confirmation response
        return render(request, 'payment_confirmation.html', {"status": "Payment initiated successfully"})
    return render(request, 'payment_initiation.html')
def reports(request):
    return render(request, 'reports.html')



def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def compliance(request):
    return render(request, 'compliance.html')



def update_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == "POST":
        vendor.name = request.POST.get('name', vendor.name)
        vendor.email = request.POST.get('email', vendor.email)
        vendor.phone_number = request.POST.get('phone_number', vendor.phone_number)
        vendor.address = request.POST.get('address', vendor.address)
        vendor.status = request.POST.get('status', vendor.status)
        vendor.save()
        return redirect('vendor_details', id=vendor_id)  # Redirect to vendor details page
    return render(request, 'update_vendor.html', {'vendor': vendor})




def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == "POST":
        # Handle form submission logic here
        vendor.name = request.POST.get('name', vendor.name)
        vendor.email = request.POST.get('email', vendor.email)
        vendor.save()
        # Redirect after successful update
        return render(request, '/vendor_details.html', {'vendor': vendor})

    # Render the edit form
    return render(request, 'edit_vendor.html', {'vendor': vendor})


@login_required
def update_profile(request):
    if request.method == "POST":
        # Handle form data to update the user's profile
        user = request.user
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.email = request.POST.get("email", user.email)
        user.save()
        return redirect('profile')  # Redirect to profile page after saving
    
    return render(request, 'update_profile.html')


def submit_purchase_order(request):
    if request.method == "POST":
        # Create a new purchase order based on submitted data
        vendor_id = request.POST.get("vendor_id")
        item = request.POST.get("item")
        quantity = request.POST.get("quantity")
        unit_price = request.POST.get("unit_price")
        total_price = float(quantity) * float(unit_price)

        # Save the purchase order (assuming PurchaseOrder model)
        purchase_order = PurchaseOrder(
            vendor_id=vendor_id,
            item=item,
            quantity=quantity,
            unit_price=unit_price,
            total_price=total_price,
        )
        purchase_order.save()

        return HttpResponse("Purchase order submitted successfully.")

    return render(request, "create_purchase.html")



def procurement(request):
    # Add necessary context for the procurement page
    return render(request, 'procurement.html')



def create_purchase(request):
    if request.method == "POST":
        # Handle form submission logic here
        vendor = request.POST.get("vendor")
        item = request.POST.get("item")
        quantity = request.POST.get("quantity")
        unit_price = request.POST.get("unit_price")
        total_price = float(quantity) * float(unit_price)

        # Save purchase order to the database if a model exists
        # Example:
        # PurchaseOrder.objects.create(vendor=vendor, item=item, quantity=quantity, unit_price=unit_price, total_price=total_price)

        return render(request, 'create_purchase.html', {"message": "Purchase order created successfully!"})

    return render(request, 'create_purchase.html')




def vendor_info(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    return render(request, 'vendor_info.html', {'vendor': vendor})
    
def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        messages.success(request, "Vendor deleted successfully.")
        return redirect('vendor_list')
    return render(request, 'confirm_delete.html', {'vendor': vendor})




def track_payments(request):
    # Add necessary context for the track payments page
    return render(request, 'track_payments.html')





def generate_report(request):
    if request.method == "POST":
        report_type = request.POST.get('reportType')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')

        # Add logic to generate the report based on the type and date range
        # For now, we return a dummy response
        return JsonResponse({'status': 'success', 'message': f'Report of type {report_type} generated successfully!'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})




def filter_payments(request):
    payment_status = request.GET.get('payment_status', 'all')
    payment_date = request.GET.get('payment_date')

    # Filter logic
    payments = Payment.objects.all()
    if payment_status != 'all':
        payments = payments.filter(status=payment_status)
    if payment_date:
        payments = payments.filter(date=payment_date)

    return render(request, 'track_payments.html', {'payments': payments})


def search_vendors(request):
    vendor_name = request.GET.get('vendorName', '')
    vendor_type = request.GET.get('vendorType', 'all')

    context = {
        'vendor_name': vendor_name,
        'vendor_type': vendor_type,
    }
    return render(request, 'search_vendors.html', context)

def mse_onboarding(request):
    return render(request, 'mse_onboarding.html')

def mse_support(request):
    return render(request, 'mse_support.html')

def contact_support(request):
    return render(request, 'contact_support.html')

def create_procurement_request(request):
    if request.method == 'POST':
        vendor = request.POST.get('vendor')
        item_details = request.POST.get('item-details')
        quantity = request.POST.get('quantity')

        # Logic to handle the procurement request (e.g., save to database)
        # Example:
        # ProcurementRequest.objects.create(vendor=vendor, item_details=item_details, quantity=quantity)

        # Redirect to a success page or back to the procurement page
        return redirect('procurement')

    # Render a template if needed (optional)
    return render(request, 'create_procurement_request.html')

def edit_profile(request):
    # Your logic for editing a profile goes here
    return render(request, 'edit_profile.html')

from django.shortcuts import render
from .models import Vendor
from django.shortcuts import get_object_or_404, redirect
from .forms import VendorForm

def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_details', vendor_id=vendor.id)
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'edit_vendor.html', {'form': form, 'vendor': vendor})

def add_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'add_vendor.html', {'form': form})


def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list')
    return render(request, 'delete_vendor.html', {'vendor': vendor})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_list.html', {'vendors': vendors})

def vendor_details(request, vendor_id):
    vendor = Vendor.objects.get(id=vendor_id)
    return render(request, 'vendor_details.html', {'vendor': vendor})
