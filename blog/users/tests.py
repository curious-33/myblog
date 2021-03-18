from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('users:create')
TOKEN_URL = reverse('users:token')


def create_user(**params):
    return get_user_model().objects.create(**params)

class PublicUserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
    
    def test_create_valid_user_success(self):
        payload = {
            'username':'testusername',
            'password':'testpasw',
            'first_name':'Test Name'
        }
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)

    def test_user_exists(self):
        payload = {'username':'testusername', 'password':'testpasw'}
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_too_short(self):
        payload = {'username':'testusername', 'password':'test'}
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            username=payload['username']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        payload = {'username':'testusername', 'password':'testpasw'}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('token', res.data)
    
    def test_create_token_invalid_credentials(self):
        create_user('username':'testusername', 'password':'testpasw')
        payload = {'username':'testusername', 'password':'wrongpass'}
        res = self.client.post(TOKEN_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)
    
    def test_create_token_no_user(self):
        payload = {'username':'testusername', 'password':'testpasw'}
        res = self.client.post(TOKEN_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)
    
    def test_create_token_missing_field(self):
        payload = {'username':'user', 'password':''}
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)
        
