import pytest
from tests.conftest import BaseTestCase


class AuthCase(BaseTestCase):
    
    def test_auth_user(self):
        data = {
            'display_name': 'amadi',
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
            'email': 'cat@gmail.com',
            'password': 'amadijustice345'
        }
        
        response = self.client.post('/api/v1/auth/register', json=data)
        message = response.get_json().get('error')
        self.assertEqual(message, 'This is an existing User')
    