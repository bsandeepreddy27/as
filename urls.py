from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Main paths
    path('', views.index, name='index'),
    path('index.html', lambda request: redirect('/')),  # Redirect index.html to /
    path('dashboard.html', lambda request: redirect('/dashboard/')),  # Redirect dashboard.html
    path('about.html', lambda request: redirect('/about/')),  # Redirect about.html to about/
    path('signup.html', lambda request: redirect('signup')),
    path('login.html', lambda request: redirect('login')),

    # App views
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),

    # Vendor-related views
    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendors/<int:vendor_id>/', views.vendor_details, name='vendor_details'),
    path('vendors/add/', views.add_vendor, name='add_vendor'),
    path('vendors/<int:vendor_id>/edit/', views.edit_vendor, name='edit_vendor'),
    path('vendors/<int:vendor_id>/delete/', views.delete_vendor, name='delete_vendor'),

    # Specific vendor views
    path('vendor/<int:vendor_id>/', views.vendor_info, name='vendor_info'),
    path('vendor/', views.vendor_list, name='vendor_list'),
    path('vendor/edit/<int:vendor_id>/', views.edit_vendor, name='edit_vendor'),
    path('vendor/delete/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),
    path('vendor/update/<int:vendor_id>/', views.update_vendor, name='update_vendor'),
    path('vendor_info/<int:vendor_id>/', views.vendor_info, name='vendor_info'),
    path('search_vendors/', views.search_vendors, name='search_vendors'),

    # Procurement-related views
    path('create_procurement_request/', views.create_procurement_request, name='create_procurement_request'),
    path('procurement/', views.procurement, name='procurement'),
    path('create_purchase/', views.create_purchase, name='create_purchase'),

    # Payment-related views
    path('payments/initiate/', views.initiate_payment, name='initiate_payment'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/<int:id>/', views.payment_details, name='payment_details'),
    path('filter_payments/', views.filter_payments, name='filter_payments'),
    path('track_payments/', views.track_payments, name='track_payments'),

    # MSE-related views
    path('mse_onboarding/', views.mse_onboarding, name='mse_onboarding'),
    path('mse_support/', views.mse_support, name='mse_support'),
    path('contact_support/', views.contact_support, name='contact_support'),

    # Report and compliance views
    path('generate_report/', views.generate_report, name='generate_report'),
    path('reports/', views.reports, name='reports'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('compliance/', views.compliance, name='compliance'),

    # Purchase-related views
    path('submit_purchase_order/', views.submit_purchase_order, name='submit_purchase_order'),
]
