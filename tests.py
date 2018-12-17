import unittest
import os
import json
from stackoverflow import create_app
from stackoverflow.config import Config
from flask import jsonify



class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(Config)
        self.client = self.app.test_client
        self.users = {
            'name':'Mwangi',
            'city':'Malindi',
        }

    def test_api_can_get_all_users(self):
        """Test API can get a Users (GET request)."""
        res = self.client().post('http://127.0.0.1:5000/users/post', data={'name':'Mwangi','city':'Malindi'})
        self.assertEqual(res.status_code, 201)
        res = self.client().get('http://127.0.0.1:5000/users/get')
        self.assertEqual(res.status_code, 200)
        self.assertIn('mwas', str(res.data))



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
