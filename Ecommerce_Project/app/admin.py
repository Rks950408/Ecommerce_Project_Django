from django.contrib import admin
from .models import Products

# Register your models here.
@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'description', 'composition', 'prodapp', 'category', 'product_image']
