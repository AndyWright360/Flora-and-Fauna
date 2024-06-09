from django.test import TestCase
from decimal import Decimal

from .models import Order, OrderLineItem
from products.models import Product, Range


class TestCheckoutModels(TestCase):

    def setUp(self):
        """ Creates test objects for Checkout app """

        self.range_test = Range.objects.create(
            name="test_range",
            friendly_name="Test Range",
        )

        self.product_test_1 = Product.objects.create(
            range=self.range_test,
            name="Test Product 1",
            category="Test Category 1",
            description="Test Description 1",
            ingredients="Test Ingredients 1",
            price=9.99,
            size="Test Size 1",
            image="test_image_1.jpg",
        )

        self.product_test_2 = Product.objects.create(
            range=self.range_test,
            name="Test Product 2",
            category="Test Category 2",
            description="Test Description 2",
            ingredients="Test Ingredients 2",
            price=19.99,
            size="Test Size 2",
            image="test_image_2.jpg",
        )

        self.order_test = Order.objects.create(
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

        self.order_line_item_test_1 = OrderLineItem.objects.create(
            order=self.order_test,
            product=self.product_test_1,
            quantity=1,
        )

        self.order_line_item_test_2 = OrderLineItem.objects.create(
            order=self.order_test,
            product=self.product_test_2,
            quantity=2,
        )

    def test_order_string_representation(self):
        """ 
        Test the string representation of an order returns its order number
        """
        order = Order(order_number='1234567890')
        self.assertEqual(str(order), order.order_number)

    def test_order_number(self):
        """ 
        Test that the order number is set correctly
        """
        self.assertEqual(self.order_test.order_number, '1234567890')

    def test_order_full_name(self):
        """ 
        Test that the order's full name is set correctly
        """
        self.assertEqual(self.order_test.full_name, 'Test User')

    def test_order_email(self):
        """ 
        Test that the order's email is set correctly
        """
        self.assertEqual(self.order_test.email, 'test@test.com')

    def test_order_phone_number(self):
        """ 
        Test that the order's phone number is set correctly
        """
        self.assertEqual(self.order_test.phone_number, '0123456789')

    def test_order_street_address_1(self):
        """ 
        Test that the order's street address 1 is set correctly
        """
        self.assertEqual(self.order_test.street_address1, 'Test Address 1')
    
    def test_order_street_address_2(self):
        """ 
        Test that the order's street address 2 is set correctly
        """
        self.assertEqual(self.order_test.street_address2, 'Test Address 2')
    
    def test_order_town_or_city(self):
        """ 
        Test that the order's town or city is set correctly
        """
        self.assertEqual(self.order_test.town_or_city, 'Test City')
    
    def test_order_county(self):
        """ 
        Test that the order's county is set correctly
        """
        self.assertEqual(self.order_test.county, 'Test County')
    
    def test_order_postcode(self):
        """ 
        Test that the order's postcode is set correctly
        """
        self.assertEqual(self.order_test.postcode, 'TE57 0NE')
    
    def test_order_country(self):
        """ 
        Test that the order's country is set correctly
        """
        self.assertEqual(self.order_test.country, 'GB')

    def test_order_total(self):
        """ 
        Test that the order total is calculated correctly
        """

        total_order_price = (
            (self.order_line_item_test_1.lineitem_total) +
            (self.order_line_item_test_2.lineitem_total)
        )
        expected_order_total = Decimal(total_order_price)

        # Round both expected and actual order totals to 2 decimal places
        expected_order_total = expected_order_total.quantize(Decimal('0.01'))
        actual_order_total = self.order_test.order_total.quantize(Decimal('0.01'))

        self.assertEqual(actual_order_total, expected_order_total)

    def test_delivery_cost_calculation(self):
        """
        Test that the delivery cost is calculated correctly
        """

        total_order_price = (
            (self.order_line_item_test_1.lineitem_total) +
            (self.order_line_item_test_2.lineitem_total)
        )
        expected_delivery_cost = Decimal(total_order_price * 0.10)

        # Round both expected and actual delivery costs to 2 decimal places
        expected_delivery_cost = expected_delivery_cost.quantize(Decimal('0.01'))
        actual_delivery_cost = self.order_test.delivery_cost.quantize(Decimal('0.01'))

        self.assertEqual(actual_delivery_cost, expected_delivery_cost)

    def test_grand_total_calculation(self):
        """ 
        Test that the grand total is calculated correctly
        """
        self.assertEqual(
            self.order_test.grand_total,
            self.order_test.order_total + self.order_test.delivery_cost)

    def test_order_line_item_order_number(self):
        """ 
        Test that the order line item has the correct order number
        """
        self.assertEqual(
            self.order_line_item_test_1.order.order_number, '1234567890')

    def test_order_line_item_product_name(self):
        """ 
        Test that the order line item has the correct product name
        """
        self.assertEqual(self.order_line_item_test_1.product.name, "Test Product 1")

    def test_order_line_item_quantity(self):
        """ 
        Test that the order line item has the correct quantity
        """
        self.assertEqual(self.order_line_item_test_1.quantity, 1)

    def test_order_line_item_total_calculation(self):
        """ 
        Test that the order line item total is calculated correctly
        """
        self.assertEqual(
            self.order_line_item_test_2.lineitem_total, (
                self.order_line_item_test_2.product.price *
                self.order_line_item_test_2.quantity)
        )
        self.assertEqual(self.order_line_item_test_2.lineitem_total, 39.98)
