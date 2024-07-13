from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Range, Product
from checkout.models import Order, OrderLineItem


class TestProductsViews(TestCase):
    """ Test products view """

    def setUp(self):
        """ Creates test objects for Products app """

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

        self.order_test = Order.objects.create(
            order_number='1234567890',
            full_name="Test User",
            email="test@test.com",
            phone_number="0123456789",
            street_address1="Test Address 1",
            street_address2="Test Address 2",
            town_or_city="Test City",
            county="Test County",
            postcode="TE57 0NE",
            country="GB",
        )

        self.order_line_item_test = OrderLineItem.objects.create(
            order=self.order_test,
            product=self.product_test,
            quantity=1,
        )

    def test_products_page(self):
        """ Test products url status code """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_page_with_valid_product(self):
        """ Test product detail page with valid product ID """
        response = self.client.get(
            reverse('product_detail', args=[self.product_test.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_page_with_invalid_product(self):
        """ Test product detail page with invalid product ID """
        response = self.client.get(reverse('product_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_add_product_redirects_logged_out_user_to_login(self):
        """ Test add product view redirects logged out user to login """
        url = reverse('add_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_add_product_view_for_unauthorised_user(self):
        """ Test add product view for unauthorised user """
        self.client.force_login(self.user_test)
        url = reverse('add_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_add_product_view_for_superuser(self):
        """ Test add product view for superuser """
        self.client.force_login(self.superuser_test)
        url = reverse('add_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_edit_product_view_for_logged_out_user(self):
        """ Test edit product view redirects logged out user to login """
        url = reverse('edit_product', args=[self.product_test.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_edit_product_view_for_unauthorised_user(self):
        """ Test edit product view for unauthorised user """
        self.client.force_login(self.user_test)
        url = reverse('edit_product', args=[self.product_test.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_edit_valid_product_view_for_superuser(self):
        """ Test edit product view for superuser with valid product """
        self.client.force_login(self.superuser_test)
        url = reverse('edit_product', args=[self.product_test.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_edit_invalid_product_view_for_superuser(self):
        """ Test edit product view for superuser with invalid product """
        self.client.force_login(self.superuser_test)
        url = reverse('edit_product', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_delete_product_view_for_logged_out_user(self):
        """ Test delete product view redirects logged out user to login """
        url = reverse('delete_product', args=[self.product_test.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={url}')

    def test_delete_product_view_for_unauthorised_user(self):
        """ Test delete product view for unauthorised user """
        self.client.force_login(self.user_test)
        url = reverse('delete_product', args=[self.product_test.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_delete_valid_product_view_for_superuser(self):
        """ Test delete product view for superuser with valid product """
        self.client.force_login(self.superuser_test)
        url = reverse('delete_product', args=[self.product_test.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products'))

    def test_delete_invalid_product_view_for_superuser(self):
        """ Test delete product view for superuser with invalid product """
        self.client.force_login(self.superuser_test)
        url = reverse('delete_product', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
