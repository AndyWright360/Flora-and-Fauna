from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile
from checkout.models import Order


class ProfileViewTests(TestCase):
    """
    Tests for Profile Views
    """

    def setUp(self):

        self.user_test = User.objects.create_user(
            username='TestUser',
            first_name='Test',
            last_name='User',
            password='TestPassword',
            email='test@test.com'
        )

        self.user_profile_test = UserProfile.objects.get(
            user=self.user_test
        )

        self.order_test = Order.objects.create(
            order_number='1234567890',
            user_profile=self.user_profile_test,
            full_name="Test User",
            email="testemail@email.com",
            phone_number="0123456789",
            street_address1="Test Address 1",
            street_address2="Test Address 2",
            town_or_city="Test City",
            county="Test County",
            country="GB"
        )

    def test_profile_page(self):
        """
        Test that the user profile page loads correctly and uses the correct template
        """
        self.client.login(username='TestUser', password='TestPassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_order_history_page(self):
        """
        Test that the order history page loads correctly and uses the correct template
        """
        self.client.login(username='TestUser', password='TestPassword')
        response = self.client.get(reverse('order_history', args=[self.order_test.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
