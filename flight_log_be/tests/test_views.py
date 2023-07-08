from django.test import TestCase
from flight_log_be.models import User
from django.test import Client
from .factories import UserFactory 
import json

class GetUserCase(TestCase):
    def setUp(self):
        users = UserFactory.create_batch(10)
        global user
        user = User.objects.last()

    def test_user_is_returned(self):
        c = Client()
        response = c.get(f'/api/v1/users/{user.id}')

        self.assertEqual(response.status_code, 200)
        
        json = json.loads(response)