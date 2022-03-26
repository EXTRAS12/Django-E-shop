from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 1


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created', 'update']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'total_price', 'customer_email',
                    'customer_phone', 'status', 'created', 'update']
    inlines = [ProductInOrderInline]


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'nmb', 'price_per_item', 'total_price', 'product', 'is_active', 'created', 'update']


admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)

