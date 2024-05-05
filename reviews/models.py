from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews',)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='reviews')
    created_on = models.DateField(auto_now_add=True, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES, null=False)

    def __str__(self):
        return self.title