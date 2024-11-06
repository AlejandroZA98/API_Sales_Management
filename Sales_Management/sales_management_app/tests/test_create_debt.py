from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from sales_management_app.api.models.clients_model import Client
from sales_management_app.api.models.debts_to_pay_model import DebtstoPay

class CreateDebttoPayTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client_instance = Client.objects.create(
            name="Cliente de prueba",
            user=self.user,
            paid_money=0,
            debt_money=0
        )
        self.url = reverse('create-debttopay', kwargs={'pk': self.user.pk})

    def test_create_debt_success(self):
        data = {
            "client": self.client_instance.id,
            "amount_sell": 500,
            "amount_paid": 200,
            "debt": 300,
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['amount_sell'], data['amount_sell'])
        self.assertEqual(response.data['amount_paid'], data['amount_paid'])
        self.assertEqual(response.data['debt'], data['debt'])
        self.assertTrue(DebtstoPay.objects.filter(id=response.data['id']).exists())

    def test_create_debt_invalid_data(self):
        data = {
            "client": self.client_instance.id,
            "amount_sell": "invalid",
            "amount_paid": 200,
            "debt": 300,
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("amount_sell", response.data)
