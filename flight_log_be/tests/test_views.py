from django.test import TestCase, Client
from flight_log_be.models import User, Flight
from .factories import UserFactory, FlightFactory
import json

class FlightCreationTestCase(TestCase):
    def test_flight_creation(self):
        user = UserFactory()
        
        flight_data = {
            'date': '2022-01-01',
            'aircraft': 'Boeing 747',
            'start_location': 'New York',
            'end_location': 'Los Angeles',
            'day_hours': 5,
            'night_hours': 3,
            'description': 'Test flight',
        }
    
        response = self.client.post(f'/api/v1/users/{user.id}/flights/',dict(flight_data))
        
        self.assertEqual(response.status_code, 201)
        
        self.assertTrue(Flight.objects.filter(user=user).exists())

class FlightCreationSadPathTestCase(TestCase):        
    def test_sad_path_flight_creation(self):
        user = UserFactory()
        
        flight_data = {
            'date': '2022-01-01',
            'aircraft': 'Boeing 747',
            'day_hours': 5,
            'night_hours': 3,
            'description': 'Test flight',
        }
    
        response = self.client.post(f'/api/v1/users/{user.id}/flights/', flight_data)
        self.assertEqual(response.status_code, 400)
        expected_response = { "errors": 
                                [
                                    {'start_location': ['This field is required.'],
                                    'end_location': ['This field is required.']}
                                ]
                            }
        self.assertEqual(response.json(), expected_response)
        
        self.assertFalse(Flight.objects.filter(user=user).exists())



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
