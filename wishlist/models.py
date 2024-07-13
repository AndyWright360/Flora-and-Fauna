from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    # Prevents duplicate items being added to a user's wishlist
    class Meta:
        unique_together = ['user', 'product']

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
