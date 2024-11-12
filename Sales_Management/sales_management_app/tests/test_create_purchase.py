from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
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

        refresh = RefreshToken.for_user(self.user)
        self.jwt_token = f"Bearer {refresh.access_token}"

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

        response = self.client.post(
            url, purchase_data, format='json', 
            HTTP_AUTHORIZATION=self.jwt_token
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')

    def test_create_purchase_with_existing_inventory(self):
        InventaryIngredients.objects.create(
            ingredient="Harina", user=self.user, cuantity=20
        )

        url = reverse('create-purchase', kwargs={'pk': self.user.pk})

        purchase_data = [
            {
                "concept": "Harina",
                "cuantity": 5,
                "unit_price": 2.5,
                "type": "compra",
                "balance": 0,
                "supplier": "Proveedor A"
            }
        ]

        response = self.client.post(
            url, purchase_data, format='json',
            HTTP_AUTHORIZATION=self.jwt_token
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'success')

