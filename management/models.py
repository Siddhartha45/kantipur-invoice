from django.db import models
from invoice import commons


class AddCustomer(models.Model):
    """for handling customer details"""
    
    customer_type = models.CharField(max_length=255, choices=commons.CUSTOMER_CHOICES, blank=True)
    primary_contact=models.CharField(max_length=255,choices=commons.SALUTATION_CHOICES)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True)
    customer_display_name=models.CharField(max_length=255)
    
    
    currency=models.CharField(max_length=255,choices=commons.CURRENCY_CHOICES)
    individual_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=255, blank=True)
    mobile=models.CharField(max_length=255)
    #other details part
    
    Portal_Language=models.CharField(max_length=255,choices=commons.LANGUAGE_CHOICES, blank=True)
    
    facebook=models.CharField( max_length=50, blank=True)
    twitter=models.CharField( max_length=50, blank=True)

    
    

    
class Invoice(models.Model):
    customer_name=models.CharField( max_length=50)
    invoice_number=models.IntegerField()
    balance_due=models.IntegerField()
    order_number=models.IntegerField()
    invoice_date=models.DateField()
    due_date=models.DateField()
    subject=models.CharField(max_length=255)
    