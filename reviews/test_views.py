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
        response = self.client.get(
            reverse('add_review', args=[self.product_test.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')

    def test_add_review_page_for_logged_out_user_redirects_to_login(self):
        """
        Test that the add review page redirects to login for logged out users
        """
        response = self.client.get(
            reverse('add_review', args=[self.product_test.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=%2Freviews%2Fadd_review%2F1/')

    def test_edit_review_page_for_authorised_user(self):
        """
        Test that the edit review page is accessible for logged in users
        """
        self.client.force_login(self.user_test)
        response = self.client.get(
            reverse('edit_review', args=[self.review_test1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/edit_review.html')

    def test_edit_review_page_for_logged_out_user_redirects_to_login(self):
        """
        Test that the edit review page redirects to login for logged out users
        """
        response = self.client.get(
            reverse('edit_review', args=[self.review_test1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=%2Freviews%2Fedit_review%2F1%2F')

    def test_edit_review_page_redirects_unauthorised_user_correctly(self):
        """
        Test that the edit review page redirects to
        product details if the user is not the author of the review
        """
        self.client.force_login(self.user_test)
        response = self.client.get(
            reverse('edit_review', args=[self.review_test2.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')

    def test_edit_review_page_redirects_superuser_correctly(self):
        """
        Test that the edit review page redirects to product details
        if the user is a superuser and not the author of the review
        """
        self.client.force_login(self.superuser_test)
        response = self.client.get(
            reverse('edit_review', args=[self.review_test1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')

    def test_delete_review_view_for_logged_out_user_redirects_to_login(self):
        """
        Test that the delete review page redirects
        to login for logged out users
        """
        response = self.client.get(
            reverse('delete_review', args=[self.review_test1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/accounts/login/?next=%2Freviews%2Fdelete_review%2F1%2F')

    def test_delete_review_page_redirects_unauthorised_user_correctly(self):
        """
        Test that the delete review page redirects to product details
        if the user is not the author of the review
        """
        self.client.force_login(self.user_test)
        response = self.client.get(
            reverse('delete_review', args=[self.review_test2.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')

    def test_adding_a_product_review_updates_product_average_rating(self):
        """
        Test that the average rating for a product
        is updated when a review is added
        """

        # Create review for the product
        self.review_test3 = Review.objects.create(
            product=self.product_test,
            user=self.user_test,
            created_on=timezone.now(),
            title="Test Title 3",
            content="Test Content 3",
            rating=4,
        )

        self.assertEqual(self.product_test.average_rating(), 4)

    def test_editing_a_product_review_updates_product_average_rating(self):
        """
        Test that the average rating for a product
        is updated when a review is edited
        """
        # Edit the review's rating
        self.review_test1.rating = 3
        self.review_test1.save()

        self.assertEqual(self.product_test.average_rating(), 3)

    def test_deleting_a_product_review_updates_product_average_rating(self):
        """
        Test that the average rating for a product
        is updated when a review is deleted
        """
        # Delete a review
        self.review_test2.delete()

        self.assertEqual(self.product_test.average_rating(), 5)
