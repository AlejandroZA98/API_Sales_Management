# users_app/tests/test_create_user.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class RegisterUserTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('register')  # Asegúrate de tener el nombre correcto en tus urls.py
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'password_2': 'testpassword123'  # Agrega el campo de confirmación
        }

    def test_user_registration(self):
        """Test para verificar que un usuario se registra correctamente."""
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('response', response.data)
        self.assertIn('token', response.data)

        # Verificamos que el usuario se haya creado
        user = User.objects.get(username=self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])

    def test_user_registration_invalid_data(self):
        """Test para verificar el registro con datos inválidos."""
        invalid_data = self.user_data.copy()
        invalid_data['email'] = ''  # Falta el email

        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Asegúrate de que el mensaje de error contenga el campo 'email'
        self.assertIn('email', response.data['details'])  # Esto debe ajustarse a la estructura real de tu respuesta
