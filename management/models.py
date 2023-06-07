from django.db import models


class AddCustomer(models.Model):
    """for handling customer details"""
    
    CUSTOMER_CHOICES = (
        ('business', 'business'),
        ('individual', 'individual'),
    )
    customer_type = models.CharField(max_length=255, choices=CUSTOMER_CHOICES)
    company_name = models.CharField(max_length=255, blank=True)
    individual_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    
    
class Payment(models.Model):
    """for handling payment types"""
    
    payment_name = models.CharField(max_length=255, unique=True)
    days = models.PositiveIntegerField()
    
    
class Package(models.Model):
    """for handling packages"""
    
    PACKAGE_CHOICES = (
        ('goods', 'goods'),
        ('service', 'service'),
    )
    package_type = models.CharField(max_length=255, choices=PACKAGE_CHOICES)
    package_name = models.CharField(max_length=255, unique=True)
    unit = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()