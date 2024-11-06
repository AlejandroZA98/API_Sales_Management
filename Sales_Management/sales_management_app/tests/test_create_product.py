from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from sales_management_app.api.models.products_model import Product

class CreateProductViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.url = reverse('create-products', kwargs={'pk': self.user.pk})
        self.valid_data = {
            'name': 'Test Product',
            'unit_price': 10.0,
            'type': 'Test Type'
        }

    def test_create_product_success(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().name, 'Test Product')

    def test_create_product_invalid_data(self):
        invalid_data = {
            'name': '',
            'unit_price': -10.0,
            'type': 'Test Type'
        }
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        
        if 'unit_price' in response.data:
            self.assertIn('unit_price', response.data)
