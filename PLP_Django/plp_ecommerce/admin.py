from django.contrib import admin # type: ignore
#First import the models you have
from .models import Customer, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)