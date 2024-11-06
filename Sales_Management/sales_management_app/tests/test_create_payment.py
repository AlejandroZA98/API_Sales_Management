from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from sales_management_app.api.models.payments_model import Payment
from sales_management_app.api.models.clients_model import Client
from django.contrib.auth.models import User

class CreatePaymentsViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client_instance = Client.objects.create(
            name="Cliente de prueba",
            user=self.user,
            paid_money=0,
            debt_money=0
        )
        self.url = reverse('create-payment', kwargs={'pk': self.user.pk})

    def test_create_payment_success(self):
        data = {
            "client": self.client_instance.id,
            "amount": 100,
            "payment_date": "2024-11-06T00:00:00Z",
            "merchandise": "Producto de prueba",
            "note": "Nota de pago de prueba"
        }
        response = self.client.post(self.url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['amount'], data['amount'])
        self.assertEqual(response.data['merchandise'], data['merchandise'])
        self.assertEqual(response.data['note'], data['note'])
        self.assertTrue(Payment.objects.filter(id=response.data['id']).exists())

    def test_create_payment_invalid_data(self):
        data = {
            "client": self.client_instance.id,
            "amount": "invalid",
            "payment_date": "2024-11-06T00:00:00Z",
            "merchandise": "Producto de prueba",
            "note": "Nota de pago de prueba"
        }
        response = self.client.post(self.url, data, format='json')
        
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("amount", response.data)

    def test_create_payment_missing_client(self):
        data = {
            "amount": 100,
            "payment_date": "2024-11-06T00:00:00Z",
            "merchandise": "Producto de prueba",
            "note": "Nota de pago de prueba"
        }
        response = self.client.post(self.url, data, format='json')
        
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("client", response.data)

    def test_create_payment_missing_amount(self):
        data = {
            "client": self.client_instance.id,
            "payment_date": "2024-11-06T00:00:00Z",
            "description": "Pago de prueba",
            "merchandise": "Producto de prueba",
            "note": "Nota de pago de prueba"
        }
        response = self.client.post(self.url, data, format='json')
        
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("amount", response.data)
