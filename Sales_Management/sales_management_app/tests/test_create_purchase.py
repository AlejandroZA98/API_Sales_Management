from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from sales_management_app.api.models.purchases_model import Purchase
from sales_management_app.api.models.inventary_ingredients_model import InventaryIngredients
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class CreatePurchaseViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_create_purchase(self):
        url = reverse('create-purchase', kwargs={'pk': self.user.pk})

        purchase_data = [
            {
                "concept": "Harina",
                "cuantity": 10,
                "unit_price": 2.5,
                "type": "compra",
                "balance": 0,
                "supplier": "Proveedor A"
            },
            {
                "concept": "Azúcar",
                "cuantity": 5,
                "unit_price": 3.0,
                "type": "compra",
                "balance": 0,
                "supplier": "Proveedor B"
            }
        ]

        response = self.client.post(url, purchase_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')

        self.assertEqual(Purchase.objects.count(), 2)
        harina_purchase = Purchase.objects.get(concept="Harina", user=self.user)
        azucar_purchase = Purchase.objects.get(concept="Azúcar", user=self.user)

        harina_inventory = InventaryIngredients.objects.get(ingredient="Harina", user=self.user)
        azucar_inventory = InventaryIngredients.objects.get(ingredient="Azúcar", user=self.user)

        self.assertEqual(harina_inventory.cuantity, 10)
        self.assertEqual(azucar_inventory.cuantity, 5)

        self.assertEqual(harina_purchase.total_amount, 25.0)  # 10 * 2.5
        self.assertEqual(azucar_purchase.total_amount, 15.0)  # 5 * 3.0
