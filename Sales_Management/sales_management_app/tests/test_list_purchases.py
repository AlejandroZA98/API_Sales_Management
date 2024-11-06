from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from sales_management_app.api.models.purchases_model import Purchase
from django.contrib.auth import get_user_model

User = get_user_model()

class PurchasesViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        Purchase.objects.create(
            user=self.user,
            concept="Harina",
            cuantity=10,
            unit_price=2.5,
            total_amount=25.0,
            type="compra",
            balance=0.0,
            supplier="Proveedor A"
        )
        Purchase.objects.create(
            user=self.user,
            concept="Azúcar",
            cuantity=5,
            unit_price=3.0,
            total_amount=15.0,
            type="compra",
            balance=0.0,
            supplier="Proveedor B"
        )

    def test_get_purchases_list(self):
        """Verificar que la vista devuelve una lista de compras correctamente."""
        url = reverse('purchases') 
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['concept'], "Harina")
        self.assertEqual(response.data[0]['cuantity'], 10)
        self.assertEqual(response.data[0]['unit_price'], 2.5)
        self.assertEqual(response.data[0]['total_amount'], 25.0)

        self.assertEqual(response.data[1]['concept'], "Azúcar")
        self.assertEqual(response.data[1]['cuantity'], 5)
        self.assertEqual(response.data[1]['unit_price'], 3.0)
        self.assertEqual(response.data[1]['total_amount'], 15.0)
