from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('compliance/', views.compliance, name='compliance'),
    path('create_purchase/', views.create_purchase_order, name='create_purchase_order'),
    path('submit_purchase_order/', views.create_purchase_order, name='submit_purchase_order'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_vendor/', views.edit_vendor, name='edit_vendor'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('', views.index, name='index'),  # Home page
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('payment_receipt/', views.payment_receipt, name='payment_receipt'),
    path('payments/', views.payments, name='payments'),
    path('payments/initiate/', views.initiate_payment, name='initiate_payment'),

    path('procurement/', views.procurement_management, name='procurement'),
    path('profile/', views.profile, name='profile'),
    path('reports/', views.reports, name='reports'),
    path('generate-report/', views.generate_report, name='generate_report'),  # Handle custom report generation
    path('signup/', views.signup_view, name='signup'),
    path('track_payments/', views.track_payments, name='track_payments'),
    path('vendor_info/', views.vendor_info, name='vendor_info'),
    path('vendor_info/<int:vendor_id>/', views.vendor_info, name='vendor_info'),
    path('vendor_details/', views.vendor_details, name='vendor_details'),
    path('vendor/', views.vendor, name='vendor'),
    
    path('vendor/<str:vendor_id>/', views.vendor_details, name='vendor_details'),
]
