from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['seller', 'name', 'price',]
    list_filter = ['seller', 'name', 'price',]
    raw_id_fields = ('seller',)