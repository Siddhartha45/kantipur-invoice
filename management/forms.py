from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm



class InvoiceForm(forms.ModelForm):
    class Meta:
        models=Invoice
        fields='__all__'
        
        
class AddCUstomerForm(forms.Form):
    #customer_type=forms.CharField()
    #primary_contact=forms.CharField()
    customer_display_name=forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    company_name = forms.CharField()
    customer_display_name = forms.CharField()
    email = forms.EmailField()
    #website=forms.CharField()
    phone = forms.CharField()
    mobile = forms.CharField()   
    
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
    
