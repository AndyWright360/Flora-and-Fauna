from django.test import TestCase


class TestProductsViews(TestCase):
    """ Test products view """

    def test_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
