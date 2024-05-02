from django.test import TestCase
from products.models import Range, Product


class TestBagViews(TestCase):
    """ Tests for bag page views """

    def setUp(self):
        """ Creates test objects for Bag app """

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

    def test_bag_page_loads_correctly(self):
        """Test if the bag page loads correctly"""
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_product_to_bag(self):
        """Test adding a product to the bag"""
        response = self.client.post(
            f'/bag/add/{self.product_test.id}/',
            {'quantity': 1, 'redirect_url': 'view_bag'}
            )

        self.assertTrue('bag' in self.client.session)
        self.assertEqual(self.client.session['bag'][str(self.product_test.id)], 1)
        self.assertRedirects(response, '/bag/')

    def test_remove_product_from_bag(self):
        """Test removing a product from the bag"""
        self.client.post(
            f'/bag/add/{self.product_test.id}/',
            {'quantity': 1, 'redirect_url': 'view_bag'}
            )

        response = self.client.post(f'/bag/remove/{self.product_test.id}/')
        self.assertFalse(str(self.product_test.id) in self.client.session['bag'])

    def test_update_product_quantity_in_bag(self):
        """Test updating the quantity of a product in the bag"""
        response = self.client.post(
            f'/bag/add/{self.product_test.id}/',
            {'quantity': 1, 'redirect_url': 'view_bag'}
            )

        self.assertTrue('bag' in self.client.session)
        self.assertEqual(self.client.session['bag'][str(self.product_test.id)], 1)
        self.assertRedirects(response, '/bag/')

        response = self.client.post(
            f'/bag/adjust/{self.product_test.id}/',
            {'quantity': 3, 'redirect_url': 'view_bag'}
            )

        self.assertTrue('bag' in self.client.session)
        self.assertEqual(self.client.session['bag'][str(self.product_test.id)], 3)
        self.assertRedirects(response, '/bag/')
