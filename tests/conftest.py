import pytest 
import unittest
from api.models import User
from api import create_app, db
from tests.test_config import Config

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class=Config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        self.data = {
            'display_name': 'amadi',
            'email': 'cat5@gmail.com',
            'password': 'amadijustice345'
        }
        """ Seed data """
        self.client.post('/api/v1/auth/register', json=self.data)
        

def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()    

