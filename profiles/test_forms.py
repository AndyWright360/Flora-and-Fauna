from django.test import TestCase
from .forms import UserProfileForm

class TestUserProfileForm(TestCase):
    """
    Test cases for the UserProfileForm
    """

    def test_form_valid_with_empty_non_required_fields(self):
        """Test that the UserProfileForm is valid with empty non-required fields"""
        form = UserProfileForm(
            {
                'default_phone_number': '',
                'default_postcode': '',
                'default_town_or_city': '',
                'default_street_address1': '',
                'default_street_address2': '',
                'default_county': '',
                'default_country': '',
            }
        )
        self.assertTrue(form.is_valid())

    def test_user_field_excluded_in_meta(self):
        """
        Test that the 'user' field is excluded from the UserProfileForm Meta class
        """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))