from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationTestCase(APITestCase):
    def testRegistration(self):
        data = {
            "username": "Nana_Aba",
            "email": "nanaaba@gmail.com",
            "password": "12345",
            "password_confirmation": "12345"
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = 'testuser', password = 'testpassword')
        
    def test_login(self):
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logout(self):
        self.token = Token.objects.get(user__username='testuser')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)