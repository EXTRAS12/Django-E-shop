from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 1


class SubAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created', 'update']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'customer_phone', 'status', 'created',
                    'update']
    inlines = [ProductInOrderInline]


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'is_active', 'created', 'update']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'update']
    inlines = [ProductImageInline]


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'is_active', 'created', 'update' ]


admin.site.register(Subscriber, SubAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)


