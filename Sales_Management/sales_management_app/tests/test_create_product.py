from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from sales_management_app.api.models.products_model import Product

User = get_user_model()

class CreateProductViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        refresh = RefreshToken.for_user(self.user)
        self.jwt_token = f"Bearer {refresh.access_token}"
        
        self.url = reverse('create-products', kwargs={'pk': self.user.pk})
        
        self.valid_data = {
            'name': 'Test Product',
            'unit_price': 10.0,
            'type': 'Test Type'
        }

    def test_create_product_success(self):
        response = self.client.post(
            self.url, self.valid_data, format='json',
            HTTP_AUTHORIZATION=self.jwt_token
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1) 
        self.assertEqual(Product.objects.first().name, 'Test Product')  

   
    def test_create_product_missing_name(self):
        invalid_data = {
            'unit_price': 10.0,
            'type': 'Test Type'
        }
        
        response = self.client.post(
            self.url, invalid_data, format='json',
            HTTP_AUTHORIZATION=self.jwt_token
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)  

    def test_create_product_missing_unit_price(self):
        invalid_data = {
            'name': 'Test Product',
            'type': 'Test Type'
        }
        
        response = self.client.post(
            self.url, invalid_data, format='json',
            HTTP_AUTHORIZATION=self.jwt_token
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('unit_price', response.data)  
