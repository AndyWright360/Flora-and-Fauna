from django.test import TestCase
from django.utils import timezone
from datetime import date
from freezegun import freeze_time

from .models import Review
from products.models import Product, Range
from django.contrib.auth.models import User


@freeze_time("2010-10-10")
class TestReviewModels(TestCase):

    def setUp(self):
        """ Creates test objects for Review app """

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

        self.user_test = User.objects.create(
            username="TestUser",
            password="TestPassword",
            email='test@test.com',
        )

        self.review_test = Review.objects.create(
            product=self.product_test,
            user=self.user_test,
            created_on=timezone.now(),
            title="Test Title",
            content="Test Content",
            rating=5,
        )
    
    def test_review_string_representation(self):
        """ 
        Test the string representation of a review returns its title
        """
        review = Review(title='Test Title')
        self.assertEqual(str(review), 'Test Title')
    
    def test_review_title(self):
        """ 
        Test that the review title is set correctly
        """
        self.assertEqual(self.review_test.title, 'Test Title')
    
    def test_review_content(self):
        """ 
        Test that the review content is set correctly
        """
        self.assertEqual(self.review_test.content, 'Test Content')
    
    def test_review_rating(self):
        """ 
        Test that the review rating is set correctly
        """
        self.assertEqual(self.review_test.rating, 5)
    
    def test_review_created_on(self):
        """ 
        Test that the review created_on is set correctly
        """
        self.assertEqual(self.review_test.created_on, date(2010, 10, 10))
    
    def test_review_product_relationship(self):
        """ 
        Test that the review is associated with the correct product
        """
        self.assertEqual(self.review_test.product, self.product_test)

    def test_review_user_relationship(self):
        """ 
        Test that the review is associated with the correct user
        """
        self.assertEqual(self.review_test.user, self.user_test)
