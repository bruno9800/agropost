from django.contrib import admin
from .models import Product, Brand

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','product_type')
    search_fields = ['name','product_type']

admin.site.register(Product)
admin.site.register(Brand)