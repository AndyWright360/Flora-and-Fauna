from django.contrib import admin
from .models import Product, Range


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'range',
        'category',
        'price',
        'size',
        'rating',
        'image',
    )

    readonly_fields = ('rating',)

    ordering = ('name',)


class RangeAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Range, RangeAdmin)