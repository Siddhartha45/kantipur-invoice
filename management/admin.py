from django.contrib import admin
from .models import AddCustomer, Package, Payment


admin.site.register(AddCustomer)
admin.site.register(Package)
admin.site.register(Payment)