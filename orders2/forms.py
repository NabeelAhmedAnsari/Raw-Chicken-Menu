from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['restaurant_name', 'Name', 'mobile', 'email']
        widgets = {
            'restaurant_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Restaurant Name', 'required': True}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manager Name'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email ID', 'required': True}),
        }
