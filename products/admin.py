from unicodedata import category
from django.contrib import admin
from .models import Product,Category, ProductVariation

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductVariation)
