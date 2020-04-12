import os
import json
import pytest
import unittest



class TestAuthorization(unittest.TestCase):
    """ Test for the user authentication """

    def test_user_signup(self):
        """Test to see user signing up"""
        res = self.test_client.post(
            '/api/v1/register',
            data=json.dumps({ "display_name": "Jerry", "email": "amadijerry@gmail.com","password": "adaka" }),
            headers={"content-type": "application/json"}
        )
        return res

    def test_user_registration(self):
        """Test post success"""
        response = self.test_user_signup()
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "User testusr created login ")