from django.test import TestCase

from .models import Order
from products.models import Product, Range


class TestCheckoutViews(TestCase):

    def setUp(self):
        """ Creates test objects for Checkout app """

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
            rating=4,
            image="test_image.jpg",
        )

        self.order = Order.objects.create(
            order_number='1234567890',
            full_name="Test User",
            email="test@test.com",
            phone_number="0123456789",
            street_address1="Test Address 1",
            street_address2="Test Address 2",
            town_or_city="Test City",
            county="Test County",
            postcode="TE57 0NE",
            country="GB",
        )

    def test_checkout_redirects_to_products_with_empty_bag(self):
        """Test that the checkout page redirects to products when the bag is empty"""

        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/', status_code=302)

    def test_checkout_page_loads_with_bag_items(self):
        """Test that the checkout page loads when the bag contains items"""

        session = self.client.session
        session['bag'] = {str(self.product_test.id): 1}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
