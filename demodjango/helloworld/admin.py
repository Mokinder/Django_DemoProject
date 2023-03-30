from django.contrib import admin
from .models import product,productcategory,bill

# Register your models here.

admin.site.register(productcategory)

admin.site.register(product)

admin.site.register(bill)

