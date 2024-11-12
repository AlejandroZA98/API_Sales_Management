from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from sales_management_app.api.models.sells_model import Sell
from sales_management_app.api.models.products_model import Product
from sales_management_app.api.models.inventary_products_model import InventaryProducts
from sales_management_app.api.models.clients_model import Client
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

class CreateSellsViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        self.access_token = str(AccessToken.for_user(self.user))
        
        self.client_instance = Client.objects.create(
            name="Cliente de prueba",
            user=self.user,
            paid_money=0,
            debt_money=0
        )
        
        self.product1 = Product.objects.create(user=self.user, name="Producto A", unit_price=100)
        self.inventory1 = InventaryProducts.objects.create(user=self.user, product=self.product1, cuantity=50)
        
        self.product2 = Product.objects.create(user=self.user, name="Producto B", unit_price=200)
        self.inventory2 = InventaryProducts.objects.create(user=self.user, product=self.product2, cuantity=30)

        self.url = reverse('create-sell', args=[self.user.pk])

    def test_create_sell_success(self):
        data = {
            "client": self.client_instance.id,
            "concept": [self.product1.id, self.product2.id],
            "details": {
                "quantities": [10, 5]
            },
            "type": "Venta",
            "amount_paid": 500,
            "debt_amount": 300,
            "balance": 200,
            "credits": 1
        }

        response = self.client.post(
            self.url, 
            data, 
            format='json', 
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.inventory1.refresh_from_db()
        self.inventory2.refresh_from_db()
        self.assertEqual(self.inventory1.cuantity, 40)  
        self.assertEqual(self.inventory2.cuantity, 25)  

        sell = Sell.objects.get(id=response.data['id'])
        expected_total_price = 10 * self.product1.unit_price + 5 * self.product2.unit_price
        self.assertEqual(response.data['total_price'], expected_total_price)
        self.assertEqual(sell.total_price, expected_total_price)

    def test_create_sell_insufficient_stock(self):
        data = {
            "client": self.client_instance.id,
            "concept": [self.product1.id, self.product2.id],
            "details": {
                "quantities": [100, 5] 
            },
            "type": "Venta",
            "amount_paid": 500,
            "debt_amount": 300,
            "balance": 200,
            "credits": 1
        }

        response = self.client.post(
            self.url, 
            data, 
            format='json', 
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("No hay suficiente stock", response.data['error'])

    def test_create_sell_mismatched_concept_and_quantity(self):
        data = {
            "client": self.client_instance.id,
            "concept": [self.product1.id], 
            "details": {
                "quantities": [10, 5]  
            },
            "type": "Venta",
            "amount_paid": 500,
            "debt_amount": 300,
            "balance": 200,
            "credits": 1
        }

        response = self.client.post(
            self.url, 
            data, 
            format='json', 
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("La cantidad de conceptos no coincide con la de cantidades", response.data['error'])

    def test_create_sell_missing_quantity(self):
        data = {
            "client": self.client_instance.id,
            "concept": [self.product1.id],
            "details": {}, 
            "type": "Venta",
            "amount_paid": 500,
            "debt_amount": 300,
            "balance": 200,
            "credits": 1
        }

        response = self.client.post(
            self.url, 
            data, 
            format='json', 
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("La cantidad de conceptos no coincide con la de cantidades", response.data['error'])
