from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from sales_management_app.api.models.sells_model import Sell
from sales_management_app.api.models.clients_model import Client  # Importa el modelo de Client
from sales_management_app.api.serializers.sells_serializer import SellSerializer
from django.contrib.auth.models import User

class SellDetailViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        self.client_instance = Client.objects.create(
            name="Cliente de prueba",
            user=self.user,
            paid_money=0,
            debt_money=0
        )
        
        self.sell = Sell.objects.create(
            user=self.user,
            client=self.client_instance,
            type="Venta",
            amount_paid=500,
            debt_amount=300,
            balance=200,
            credits=1,
            details={}
        )

        self.url = reverse('sell-detail', kwargs={'pk': self.sell.pk})

    def test_get_sell_detail_success(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        serializer = SellSerializer(self.sell, context={'request': response.wsgi_request})
        self.assertEqual(response.data, serializer.data)

