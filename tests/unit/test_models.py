import pytest 
import unittest
from api.models import User
from api import create_app, db
from tests.test_config import Config

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class=Config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()    

    def test_password_salts_are_random(self):
        u = User(email='cat@gmail.com')
        u.set_password('cat')
        u2 = User(email='cat2@gmail.com')
        u.set_password('cat')
        self.assertTrue(u.password_hash != u2.password_hash)