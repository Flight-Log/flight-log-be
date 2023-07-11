from django.test import TestCase
from flight_log_be.models import User
from django.test import Client
from .factories import UserFactory 
import json

class GetUserCase(TestCase):
    def setUp(self):
        users = UserFactory.create_batch(10)
        global user
        user = User.objects.order_by('?').first()
        global c
        c = Client()

    def test_user_is_returned(self):
        response = c.get(f'/api/v1/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        
        returned_user = json.loads(response.content)["data"]

        self.assertEqual(returned_user["id"], f"{user.id}")
        self.assertEqual(returned_user["type"], "user")
        self.assertEqual(returned_user["attributes"]["first_name"], user.first_name)
        self.assertEqual(returned_user["attributes"]["last_name"], user.last_name)
    
    def test_error_is_returned(self):
        response = c.get(f'/api/v1/users/104234')
        self.assertEqual(response.status_code, 404)
        
        returned_error = json.loads(response.content)

        self.assertEqual(returned_error["errors"][0]["detail"], "User not found.")
        self.assertEqual(len(returned_error["errors"]), 1)
        self.assertNotIn("id", returned_error)
        self.assertNotIn("type", returned_error)
        self.assertNotIn("attributes", returned_error)