from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, Range
from .models import WishlistItem


class WishlistItemModelTests(TestCase):
    """
    Tests for WishlistItem model
    """

    def setUp(self):
        """ Creates test objects for Wishlist app """

        self.user_test = User.objects.create(
            username="TestUser",
            password="TestPassword",
            email='test@test.com',
        )

        self.range_test = Range.objects.create(
            name="test_range",
            friendly_name="Test Range",
        )

        self.product_test = Product.objects.create(
            range=self.range_test,
            name="Test Product",
            category="Test Category",
            description="Test Description",
            ingredients="Test Ingredients",
            price=9.99,
            size="Test Size",
            image="test_image.jpg",
        )

        self.wishlist_item_test = WishlistItem.objects.create(
            user=self.user_test,
            product=self.product_test,
        )

    def test_string_representation(self):
        """
        Test the string representation of a wishlist item
        """
        self.assertEqual(str(self.wishlist_item_test), "TestUser's Wishlist")

    def test_wishlist_item_creation(self):
        """
        Test creating a wishlist item
        """
        self.assertEqual(WishlistItem.objects.count(), 1)
