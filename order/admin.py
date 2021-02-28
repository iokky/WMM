from django.contrib import admin

from .models import Category, Order, Product


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = [
        'id',
        'category',
        'name'
    ]


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = [
        'id',
        'category',
        'price',
        'date',
    ]
