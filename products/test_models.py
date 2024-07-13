from django.test import TestCase
from .models import Range, Product
from reviews.models import Review
from django.contrib.auth.models import User


class TestProductsModels(TestCase):

    def setUp(self):
        """
        Creates test objects for Products app
        """

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

        self.user_test1 = User.objects.create(
            username="TestUser1",
            password="TestPassword1",
            email='test1@test.com',
        )

        self.user_test2 = User.objects.create(
            username="TestUser2",
            password="TestPassword2",
            email='test2@test.com',
        )

    def test_range_string_method(self):
        """
        Tests the string method on the range model
        """
        self.assertEqual(str(self.range_test), self.range_test.name)

    def test_get_friendly_name_method(self):
        """
        Test get_friendly_name() method on the range model
        """
        self.assertEqual(str(
            self.range_test.get_friendly_name()),
            self.range_test.friendly_name)

    def test_product_string_method(self):
        """
        Tests the string method on the product model
        """
        self.assertEqual(str(self.product_test), self.product_test.name)

    def test_range_name(self):
        """
        Test the range name
        """
        self.assertEqual(self.range_test.name, 'test_range')

    def test_range_friendly_name(self):
        """
        Test the range friendly name
        """
        self.assertEqual(self.range_test.friendly_name, 'Test Range')

    def test_product_name(self):
        """
        Test the product name
        """
        self.assertEqual(self.product_test.name, 'Test Product')

    def test_product_category(self):
        """
        Test the product category
        """
        self.assertEqual(self.product_test.category, 'Test Category')

    def test_product_description(self):
        """
        Test the product description
        """
        self.assertEqual(self.product_test.description, 'Test Description')

    def test_product_ingredients(self):
        """
        Test the product ingredients
        """
        self.assertEqual(self.product_test.ingredients, 'Test Ingredients')

    def test_product_price(self):
        """
        Test the product price
        """
        self.assertEqual(self.product_test.price, 9.99)

    def test_product_size(self):
        """
        Test the product size
        """
        self.assertEqual(self.product_test.size, 'Test Size')

    def test_product_image(self):
        """
        Test the product image
        """
        self.assertEqual(self.product_test.image, 'test_image.jpg')

    def test_average_rating_with_no_reviews(self):
        """
        Test average rating when there are no reviews
        """
        avg_rating = self.product_test.average_rating()
        self.assertIsNone(avg_rating)

    def test_average_rating_with_reviews(self):
        """
        Test average rating when there are reviews
        """

        # Create reviews for the product
        Review.objects.create(
            product=self.product_test,
            user=self.user_test1,
            title="Great product",
            content="Love it!",
            rating=5,
        )

        Review.objects.create(
            product=self.product_test,
            user=self.user_test2,
            title="Not bad",
            content="It's okay",
            rating=3,
        )

        avg_rating = self.product_test.average_rating()
        self.assertAlmostEqual(avg_rating, 4, places=0)
