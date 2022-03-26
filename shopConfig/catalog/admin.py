from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']


class SubAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'category', 'created', 'update']
    inlines = [ProductImageInline]


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'is_active', 'created', 'update' ]


admin.site.register(Subscriber, SubAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin )


