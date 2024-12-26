# forms.py

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import ProcurementRequest, Vendor

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class ProcurementRequestForm(forms.ModelForm):
    class Meta:
        model = ProcurementRequest
        fields = ['vendor', 'item_details', 'quantity', 'urgency']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendor'].queryset = Vendor.objects.all()  # Show all available vendors in the dropdown