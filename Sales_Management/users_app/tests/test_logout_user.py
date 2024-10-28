from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.urls import reverse

class LogoutUserTest(APITestCase):

    def setUp(self):
        # Crear un usuario y generar un token de refresh para la prueba
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='password123'
        )
        self.client = APIClient()
        self.logout_url =reverse('logout')

        # Generar el token de refresh del usuario
        self.refresh_token = str(RefreshToken.for_user(self.user))

    def test_logout_success(self):
        """Verificar que el logout con un token válido funciona correctamente."""
        response = self.client.post(self.logout_url, {'refresh_token': self.refresh_token}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['detail'], 'Logged out successfully.')

    def test_logout_invalid_token(self):
        """Verificar que un token inválido genera error 400."""
        response = self.client.post(self.logout_url, {'refresh_token': 'invalid_token'}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('detail', response.data)

    def test_logout_missing_token(self):
        """Verificar que falta de token también genera error 400."""
        response = self.client.post(self.logout_url, {}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('detail', response.data)
