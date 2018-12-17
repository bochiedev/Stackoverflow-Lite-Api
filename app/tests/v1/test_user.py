import unittest
import os
import json
from app import create_app
from instance.config import Config

class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = create_app(Config)
        self.client = self.app.test_client()
        self.data = {
            'id':1,
            'username':'Mwangi',
            'email':'Malindi@gmail.com',
            'confirm_password':'Malindi@gmail.com',
            'password':'Malindi@gmail.com',

        }

    def test_api_can_register_user(self):
        """Test API can get a Users (GET request)."""
        res = self.client.post('http://127.0.0.1:5000/api/v1/post', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(res.status_code, 201)
        # res = self.client().get('http://127.0.0.1:5000/users/get')
        # self.assertEqual(res.status_code, 200)
        # self.assertIn('mwas', str(res.data))

    # def test_api_can_get_all_users(self):
    #     res = self.client.get('http://127.0.0.1:5000/api/v1/get')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(res.json['users'], 200)




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
