from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product, Range
from .models import WishlistItem


class WishlistViewsTestCase(TestCase):
    """ Test wishlist view """

    def setUp(self):
        """ Creates test objects for Wishlist app """

        self.user_test = User.objects.create_user(
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

        self.client.force_login(self.user_test)

        self.wishlist_item_test = WishlistItem.objects.create(
            user=self.user_test,
            product=self.product_test,
        )

    def test_add_to_wishlist_url_status(self):
        """ Test add wishlist url status code """
        response = self.client.get(
            reverse("add_to_wishlist"), {"id": self.product_test.id}
        )
        self.assertEqual(response.status_code, 200)

    def test_remove_from_wishlist_url_status(self):
        """ Test add wishlist url status code """
        response = self.client.get(
            reverse("remove_from_wishlist"), {"id": self.product_test.id}
        )
        self.assertEqual(response.status_code, 200)

    def test_add_to_wishlist(self):
        """ Test adding an item to the wishlist """
        response = self.client.get(
            reverse("add_to_wishlist"), {"id": self.product_test.id}
        )
        self.assertEqual(WishlistItem.objects.count(), 1)
        self.assertEqual(
            WishlistItem.objects.first().product, self.product_test)
        self.assertEqual(WishlistItem.objects.first().user, self.user_test)

    def test_remove_from_wishlist(self):
        """ Test removing an item from the wishlist """
        response = self.client.get(
            reverse("remove_from_wishlist"), {"id": self.product_test.id}
        )
        self.assertEqual(WishlistItem.objects.count(), 0)
