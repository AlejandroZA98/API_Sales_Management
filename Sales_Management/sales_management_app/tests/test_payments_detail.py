from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from sales_management_app.api.models.payments_model import Payment
from sales_management_app.api.models.clients_model import Client  # Importa el modelo de Client
from django.contrib.auth.models import User

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

        self.url = reverse('payment-detail', kwargs={'pk': self.payment.pk})

    def test_get_payment_success(self):
        response = self.client.get(self.url)
        
        # Verificar que la respuesta sea 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verificar que la respuesta contenga los datos correctos
        self.assertEqual(response.data['amount'], self.payment.amount)
        self.assertEqual(response.data['merchandise'], self.payment.merchandise)
        self.assertEqual(response.data['note'], self.payment.note)

    def test_get_payment_not_found(self):
        # Probar con un ID de pago que no existe
        url_not_found = reverse('payment-detail', kwargs={'pk': 9999})
        response = self.client.get(url_not_found)
        
        # Verificar que la respuesta sea 404 NOT FOUND
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Payment not found')

    def test_update_payment_success(self):
        updated_data = {
            "user":self.user.id,
            "client": self.client_instance.id,  
            "amount": 200,
            "merchandise": "Producto actualizado",
            "note": "Nota actualizada"
        }

        response = self.client.put(self.url, updated_data, format='json')

        print("Response Data ACTUALIZADA:", response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['amount'], updated_data['amount'])
        self.assertEqual(response.data['merchandise'], updated_data['merchandise'])
        self.assertEqual(response.data['note'], updated_data['note'])

        self.payment.refresh_from_db()
        self.assertEqual(self.payment.amount, updated_data['amount'])
        self.assertEqual(self.payment.merchandise, updated_data['merchandise'])
        self.assertEqual(self.payment.note, updated_data['note'])

    def test_update_payment_invalid_data(self):
        updated_data = {
            "client": self.client_instance.id,
            "amount": "invalid",  
            "merchandise": "Producto actualizado",
            "note": "Nota actualizada"
        }

        response = self.client.put(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        self.assertIn("amount", response.data)
