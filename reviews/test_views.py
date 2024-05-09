from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import date
from freezegun import freeze_time

from .models import Review
from products.models import Product, Range
from django.contrib.auth.models import User


@freeze_time("2010-10-10")
class TestReviewViews(TestCase):

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
            rating=4,
            image="test_image.jpg",
        )

        self.user_test = User.objects.create_user(
            username="TestUser",
            password="TestPassword",
            email='test@test.com',
        )

        self.superuser_test = User.objects.create_superuser(
            username="TestSuperUser",
            password="TestSuperPassword",
            email='testsuper@test.com',
        )

        self.review_test1 = Review.objects.create(
            product=self.product_test,
            user=self.user_test,
            created_on=timezone.now(),
            title="Test Title",
            content="Test Content",
            rating=5,
        )

        self.review_test2 = Review.objects.create(
            product=self.product_test,
            user=self.superuser_test,
            created_on=timezone.now(),
            title="Test Title 2",
            content="Test Content 2",
            rating=3,
        )

    def test_add_review_page_for_authorised_user(self):
        """ 
        Test that the add review page is accessible for logged in users
        """
        self.client.force_login(self.user_test)
        response = self.client.get(reverse('add_review', args=[self.product_test.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')

    def test_add_review_page_for_logged_out_user_redirects_to_login(self):
        """ 
        Test that the add review page redirects to login for logged out users
        """
        response = self.client.get(reverse('add_review', args=[self.product_test.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=%2Freviews%2Fadd_review%2F1/')

    def test_edit_review_page_for_authorised_user(self):
        """ 
        Test that the edit review page is accessible for logged in users
        """
        self.client.force_login(self.user_test)
        response = self.client.get(reverse('edit_review', args=[self.review_test1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/edit_review.html')

    def test_edit_review_page_for_logged_out_user_redirects_to_login(self):
        """ 
        Test that the edit review page redirects to login for logged out users
        """
        response = self.client.get(reverse('edit_review', args=[self.review_test1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=%2Freviews%2Fedit_review%2F1%2F')

    def test_edit_review_page_for_unauthorised_user_redirects_to_product_details(self):
        """ 
        Test that the edit review page redirects to product details if the user is not the author of the review
        """
        self.client.force_login(self.user_test)
        response = self.client.get(reverse('edit_review', args=[self.review_test2.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')

    def test_edit_other_user_review_page_for_superuser_redirects_to_product_details(self):
        """ 
        Test that the edit review page redirects to product details if the user is a superuser and not the author of the review
        """
        self.client.force_login(self.superuser_test)
        response = self.client.get(reverse('edit_review', args=[self.review_test1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')

    def test_delete_review_view_for_logged_out_user_redirects_to_login(self):
        """ 
        Test that the delete review page redirects to login for logged out users
        """
        response = self.client.get(reverse('delete_review', args=[self.review_test1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=%2Freviews%2Fdelete_review%2F1%2F')

    def test_delete_review_page_for_unauthorised_user_redirects_to_product_details(self):
        """ 
        Test that the delete review page redirects to product details if the user is not the author of the review
        """
        self.client.force_login(self.user_test)
        response = self.client.get(reverse('delete_review', args=[self.review_test2.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')
