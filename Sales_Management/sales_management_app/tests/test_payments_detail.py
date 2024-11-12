from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from sales_management_app.api.models.payments_model import Payment
from sales_management_app.api.models.clients_model import Client
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class PaymentDetailViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        self.client_instance = Client.objects.create(
            name="Cliente de prueba",
            user=self.user,
            paid_money=0,
            debt_money=0
        )
        
        self.payment = Payment.objects.create(
            user=self.user,
            client=self.client_instance,
            amount=100,
            merchandise="Producto de prueba",
            note="Nota de prueba"
        )

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.url = reverse('payment-detail', kwargs={'pk': self.payment.pk})

    def test_update_payment_success(self):
        updated_data = {
            "user": self.user.id,
            "client": self.client_instance.id,  
            "amount": 200,
            "merchandise": "Producto actualizado",
            "note": "Nota actualizada"
        }

        response = self.client.put(
            self.url, 
            updated_data, 
            format='json', 
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['amount'], updated_data['amount'])
        self.assertEqual(response.data['merchandise'], updated_data['merchandise'])
        self.assertEqual(response.data['note'], updated_data['note'])

        self.payment.refresh_from_db()
        self.assertEqual(self.payment.amount, updated_data['amount'])
        self.assertEqual(self.payment.merchandise, updated_data['merchandise'])
        self.assertEqual(self.payment.note, updated_data['note'])
