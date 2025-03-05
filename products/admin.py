from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'description', 'price']
    list_filter = ['available']
    search_fields = ['name', 'description', 'price']
    
admin.site.register(Product, ProductAdmin)