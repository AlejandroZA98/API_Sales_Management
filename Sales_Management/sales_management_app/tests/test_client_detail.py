from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from sales_management_app.api.models.clients_model import Client
from datetime import datetime

User = get_user_model()

class ClientDetailViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123') 

        self.client_obj = Client.objects.create(
            user=self.user,
            name='John Doe',
            paid_money=100.0,
            debt_money=50.0
        )
        self.url = reverse('client-detail', kwargs={'pk': self.client_obj.pk}) 

    def test_get_client_success(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_get_client_not_found(self):
        url = reverse('client-detail', kwargs={'pk': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {'error': 'Client not found'})

    def test_update_client_success(self):
        updated_data = {
            'user': self.user.pk,
            'name': 'Ricardo',
            'paid_money': 10.0,
            'debt_money': 0.0,
            'created_at': self.client_obj.created_at.isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        response = self.client.put(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.client_obj.refresh_from_db()
        self.assertEqual(self.client_obj.name, 'Ricardo')

    def test_update_client_not_found(self):
        url = reverse('client-detail', kwargs={'pk': 999})
        response = self.client.put(url, {'name': 'New Name', 'user': self.user.pk}, format='json')
        self.assertEqual(response.status_code, 404)

    def test_delete_client_success(self):
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Client.objects.count(), 0)

    def test_delete_client_not_found(self):
        url = reverse('client-detail', kwargs={'pk': 999})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)
