from django.contrib import admin
from .models import WishlistItem


class WishlistAdmin(admin.ModelAdmin):

    list_display = ('user', 'product', 'date_added',)


admin.site.register(WishlistItem, WishlistAdmin)
