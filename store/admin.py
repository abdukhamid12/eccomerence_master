from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'decscription']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'decscription', 'price', 'image', 'category']
