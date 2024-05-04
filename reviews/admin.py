from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):

    readonly_fields = ('product', 'title',
                       'content', 'rating',
                       'created_on',)

    list_display = ('product', 'title', 'rating',
                    'created_on',)

admin.site.register(Review, ReviewAdmin)