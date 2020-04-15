import pytest
from tests.conftest import BaseTestCase


class AuthCase(BaseTestCase):
    
    def test_auth_user(self):
        data = {
            'display_name': 'ajau',
            'email': 'amadigg@yahoo.com',
            'password': 'amadijustuce3'
        }
        
        response = self.client.post('/api/v1/auth/register', json=data)
        message = response.get_json().get('message')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(message, 'Account Creation Successful')
        
    def test_invalid_email(self):
        data = {
            'display_name': 'amadi',
            'email': 'amadi@yahoocom',
            'password': 'amadihgsg4546'
        }
        
        response = self.client.post('/api/v1/auth/register', json=data)
        message = response.get_json().get('error')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(message, 'Provide a valid email address')
        
    def test_existing_user(self):
        data = {
            'display_name': 'amadi',
            'email': 'cat5@gmail.com',
            'password': 'amadijustice345'
        }
        
        response = self.client.post('/api/v1/auth/register', json=data)
        message = response.get_json().get('error')
        self.assertEqual(message, 'This is an existing User')
    
    def login_user(self):
        data = {
            'email': 'cat5@gmail.com',
            'password': 'amadijustice345'
        }
        
        response = self.client.post('/api/v1/auth/login', json=data)
        self.assertEqual(response.status_code, 200)
        message = response.get_json().get('message')
        self.assertEqual(message, 'Login Successful!')
        
        def test_non_existing_user(self):
            data = {
            'email': 'cattie24@gmail.com',
            'password': 'amadijustice345'
        }

        response = self.client.post('/api/v1/auth/login', json=data)
        self.assertEqual(response.status_code, 404)
        message = response.get_json().get('error')
        self.assertEqual(message, 'User does not exist!')

    def test_bad_password(self):
        data = {
            'display_name': 'amadi',
            'email': 'cat5@gmail.com',
            'password': 'amadijustice5'
        }

        response = self.client.post('/api/v1/auth/login', json=data)
        self.assertEqual(response.status_code, 400)
        message = response.get_json().get('error')
        self.assertEqual(message, 'Invalid Login Credentials!')
