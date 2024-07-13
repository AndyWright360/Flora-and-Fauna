from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserProfile


class TestUserProfileModels(TestCase):
    """
    Test cases for the UserProfile model
    """

    def setUp(self):
        """ Creates test objects for Profiles app """

        self.user_test = User.objects.create_user(
            username='TestUser',
            first_name='Test',
            last_name='User',
            password='TestPassword',
            email='test@test.com'
        )

        self.user_test.userprofile.default_phone_number = "0123456789"
        self.user_test.userprofile.default_street_address1 = "Test Address 1"
        self.user_test.userprofile.default_street_address2 = "Test Address 2"
        self.user_test.userprofile.default_town_or_city = "Test City"
        self.user_test.userprofile.default_county = "Test County"
        self.user_test.userprofile.default_postcode = "TE57 0NE"
        self.user_test.userprofile.default_country = "GB"

        self.user_test.userprofile.save()

    def test_userprofile_str_method_returns_username(self):
        """
        Test that the string representation of UserProfile returns the username
        """
        profile = UserProfile(user=self.user_test)
        self.assertEqual(str(profile), profile.user.username)

    def test_default_phone_number_is_correct(self):
        """
        Test that the 'default_phone_number' field
        is correctly saved and retrieved
        """
        profile = UserProfile.objects.get(user=self.user_test)
        self.assertEqual(profile.default_phone_number, '0123456789')

    def test_default_street_address1_is_correct(self):
        """
        Test that the 'default_street_address1' field
        is correctly saved and retrieved
        """
        profile = UserProfile.objects.get(user=self.user_test)
        self.assertEqual(profile.default_street_address1, 'Test Address 1')

    def test_default_street_address2_is_correct(self):
        """
        Test that the 'default_street_address2' field
        is correctly saved and retrieved
        """
        profile = UserProfile.objects.get(user=self.user_test)
        self.assertEqual(profile.default_street_address2, 'Test Address 2')

    def test_default_town_or_city_is_correct(self):
        """
        Test that the 'default_town_or_city' field
        is correctly saved and retrieved
        """
        profile = UserProfile.objects.get(user=self.user_test)
        self.assertEqual(profile.default_town_or_city, 'Test City')

    def test_default_county_is_correct(self):
        """
        Test that the 'default_county' field is correctly saved and retrieved
        """
        profile = UserProfile.objects.get(user=self.user_test)
        self.assertEqual(profile.default_county, 'Test County')

    def test_default_postcode_is_correct(self):
        """
        Test that the 'default_postcode' field is correctly saved and retrieved
        """
        profile = UserProfile.objects.get(user=self.user_test)
        self.assertEqual(profile.default_postcode, 'TE57 0NE')

    def test_default_country_is_correct(self):
        """
        Test that the 'default_country' field is correctly saved and retrieved
        """
        profile = UserProfile.objects.get(user=self.user_test)
        self.assertEqual(profile.default_country.code, 'GB')
