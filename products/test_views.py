from django.test import TestCase
from .models import Range, Product


class TestProductsViews(TestCase):
    """ Test products view """

    def setUp(self):
        """ Creates test objects for Products app """

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

    def test_products_page(self):
        """ Test products url status code """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
    
    def test_products_details_page_with_valid_product(self):
        """ Test product details url status code with valid product id """
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
    
    def test_products_details_page_with_invalid_product(self):
        """ Test product details url status code with invalid product id """
        response = self.client.get('/products/2/')
        self.assertEqual(response.status_code, 404)
