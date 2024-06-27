from django.test import TestCase
from .forms import ProductForm
from .models import Range, Product

class TestProductForm(TestCase):
    """
    Test cases for the ProductForm
    """

    def setUp(self):
        """ Creates test objects for Products app """
        self.range_test = Range.objects.create(
            name="test_range",
            friendly_name="Test Range",
        )

    def test_product_name_field_is_required(self):
        """Test that the 'name' field is required in ProductForm"""
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_description_field_is_required(self):
        """Test that the 'description' field is required in ProductForm"""
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_product_price_field_is_required(self):
        """Test that the 'price' field is required in ProductForm"""
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_form_valid_with_non_required_fields_empty(self):
        """Test that the form is valid even if non-required fields are empty"""
        form = ProductForm(
            {
                'name': 'Test Product',
                'description': 'Test Description',
                'price': '9.99',
                'category': 'Test Category',
                'ingredients': 'Test Ingredients',
                'size': 'Test Size',
                'range': self.range_test.id
            }
        )
        self.assertTrue(form.is_valid())

    def test_choices_for_range_field(self):
        """Test that the 'range' field choices are correctly set in ProductForm"""
        form = ProductForm()
        self.assertEqual(form.fields['range'].choices, [(self.range_test.id, 'Test Range')])
