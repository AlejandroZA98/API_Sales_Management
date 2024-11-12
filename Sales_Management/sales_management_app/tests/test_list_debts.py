from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken  
from sales_management_app.api.models.clients_model import Client
from sales_management_app.api.models.debts_to_pay_model import DebtstoPay

class DebtstoPayDetailViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        self.client_instance = Client.objects.create(
            name="Cliente de prueba",
            user=self.user,
            paid_money=0,
            debt_money=0
        )

        self.debt = DebtstoPay.objects.create(
            user=self.user,
            client=self.client_instance,
            amount_sell=500,
            amount_paid=200,
            debt=300
        )

        self.url = reverse('debtstopay-detail', kwargs={'pk': self.debt.pk})

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    def test_get_debt_detail_success(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount_sell'], self.debt.amount_sell)
        self.assertEqual(response.data['amount_paid'], self.debt.amount_paid)
        self.assertEqual(response.data['debt'], self.debt.debt)

    def test_get_debt_detail_not_found(self):
        url = reverse('debtstopay-detail', kwargs={'pk': 999})
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Debt to Pay not found')

    def test_update_debt_success(self):
        updated_data = {
            "user": self.user.id,
            "client": self.client_instance.id,
            "amount_sell": 700,
            "amount_paid": 300,
            "debt": 400
        }

        response = self.client.put(self.url, updated_data, format='json', HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.debt.refresh_from_db()
        self.assertEqual(self.debt.amount_sell, updated_data['amount_sell'])
        self.assertEqual(self.debt.amount_paid, updated_data['amount_paid'])
        self.assertEqual(self.debt.debt, updated_data['debt'])

    def test_update_debt_invalid_data(self):
        invalid_data = {
            "client": self.client_instance.id,
            "amount_sell": "invalid",  
            "amount_paid": 300,
            "debt": 400
        }

        response = self.client.put(self.url, invalid_data, format='json', HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("amount_sell", response.data)

    def test_delete_debt_success(self):
        response = self.client.delete(self.url, HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(DebtstoPay.objects.filter(pk=self.debt.pk).exists())
