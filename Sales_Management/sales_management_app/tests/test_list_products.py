from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from sales_management_app.api.models.products_model import Product
from django.contrib.auth.models import User

class ProductDetailViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.product = Product.objects.create(
            user=self.user,
            name='Test Product',
            unit_price=10.0,
            type='Test Type'
        )
        
        self.url = reverse('product-detail', kwargs={'pk': self.product.pk})

    def test_get_product(self):
        """Verificar que se puede obtener un producto existente."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product')

    def test_get_product_not_found(self):
        """Verificar que se recibe un error 404 al obtener un producto que no existe."""
        url = reverse('product-detail', kwargs={'pk': 999})  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'error': 'Product not found'})

    def test_update_product(self):
        """Verificar que se puede actualizar un producto existente."""
        updated_data = {
            'user': self.user.pk,
            'name': 'Updated Product',
            'unit_price': 15.0,
            'type': 'Updated Type'
        }
        response = self.client.put(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')

    def test_update_product_not_found(self):
        """Verificar que se recibe un error 404 al actualizar un producto que no existe."""
        url = reverse('product-detail', kwargs={'pk': 999})  
        updated_data = {
            'user': self.user.pk,
            'name': 'Updated Product',
            'unit_price': 15.0,
            'type': 'Updated Type'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product(self):
        """Verificar que se puede eliminar un producto existente."""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_delete_product_not_found(self):
        """Verificar que se recibe un error 404 al eliminar un producto que no existe."""
        url = reverse('product-detail', kwargs={'pk': 999})  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'error': 'Product not found'})
