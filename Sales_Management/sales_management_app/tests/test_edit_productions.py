from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from sales_management_app.api.models.production_model import Production
from sales_management_app.api.models.inventary_ingredients_model import InventaryIngredients
from sales_management_app.api.serializers.production_serializer import ProductionSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken  
class ProductionDetailViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        
        self.ingredient1 = InventaryIngredients.objects.create(
            user=self.user,
            ingredient="Tomate",
            cuantity=50
        )
        self.ingredient2 = InventaryIngredients.objects.create(
            user=self.user,
            ingredient="Cebolla",
            cuantity=30
        )

        self.production = Production.objects.create(
            user=self.user,
            concept="Salsa de prueba",
            cuantity=5,
            ingredients={"Tomate": 3, "Cebolla": 2}
        )

        self.url = reverse('production-detail', kwargs={'pk': self.production.pk})

    def test_get_production_detail_success(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        serializer = ProductionSerializer(self.production, context={'request': response.wsgi_request})
        self.assertEqual(response.data, serializer.data)

    def test_get_production_detail_not_found(self):
        url = reverse('production-detail', args=[999])
        
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Production not found')

    def test_delete_production_success(self):
        initial_tomate_quantity = self.ingredient1.cuantity
        initial_cebolla_quantity = self.ingredient2.cuantity
        
        response = self.client.delete(self.url, HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        self.assertFalse(Production.objects.filter(id=self.production.id).exists())

        self.ingredient1.refresh_from_db()
        self.ingredient2.refresh_from_db()
        
        expected_tomate_quantity = initial_tomate_quantity + (3 * self.production.cuantity)
        expected_cebolla_quantity = initial_cebolla_quantity + (2 * self.production.cuantity)
        
        self.assertEqual(self.ingredient1.cuantity, expected_tomate_quantity)
        self.assertEqual(self.ingredient2.cuantity, expected_cebolla_quantity)

    def test_delete_production_not_found(self):
        url = reverse('production-detail', args=[999])
        
        response = self.client.delete(url, HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'production not found')
