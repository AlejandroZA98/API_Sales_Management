from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from sales_management_app.api.models.clients_model import Client

User = get_user_model()

class ClientsViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')  

      
        Client.objects.create(user=self.user, name='John Doe', paid_money=100.0, debt_money=50.0)
        Client.objects.create(user=self.user, name='Jane Smith', paid_money=150.0, debt_money=75.0)

    def test_list_clients_success(self):
        """Verificar que se pueda listar los clientes correctamente."""
        url = reverse('clients')  
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(len(response.data), 2)  
