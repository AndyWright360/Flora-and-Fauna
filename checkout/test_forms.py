from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_order_full_name_is_required(self):
        """ Test the full name input is a required field """
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    def test_order_email_is_required(self):
        """ Test the email input is a required field """
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
    
    def test_order_phone_number_is_required(self):
        """ Test the phone number input is a required field """
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

    def test_order_street_address1_is_required(self):
        """ Test the street address 1 input is a required field """
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0], 'This field is required.')

    def test_order_town_or_city_is_required(self):
        """ Test the town or city input is a required field """
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')

    def test_order_country_is_required(self):
        """ Test the country input is a required field """
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')
    
    def test_order_not_required_inputs(self):
        """
        Test that the form can be submitted with empty non-required inputs
        """
        form = OrderForm(
            {
                'full_name': 'Test User',
                'email': 'test@test.com',
                'phone_number': '0123456789',
                'street_address1': 'Test Address 1',
                'street_address2': '',
                'town_or_city': 'Test Town',
                'county': '',
                'postcode': '',
                'country': 'GB',
            }
        )
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that only the specified fields are displayed on form
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county')
        )
