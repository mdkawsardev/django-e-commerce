from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug', 'category_image']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'slug', 'category', 'price']
@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']