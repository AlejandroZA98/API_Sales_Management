from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from sales_management_app.api.models.clients_model import Client

User = get_user_model()

class CreateClientsViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.valid_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'paid_money': 0.0,
            'debt_money': 0.0,
        }

        self.invalid_data = {
            'email': 'john.doe@example.com',
            'phone': '1234567890',
        }

    def test_create_client_success(self):
        url = reverse('create-clients', kwargs={'pk': self.user.pk})
        response = self.client.post(url, self.valid_data, format='json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.first().name, 'John Doe')

    def test_create_client_invalid_data(self):
        url = reverse('create-clients', kwargs={'pk': self.user.pk})
        response = self.client.post(url, self.invalid_data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertIn('name', response.data)  
        self.assertIn('paid_money', response.data)  
