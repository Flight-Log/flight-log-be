from django.test import TestCase, Client
from flight_log_be.models import User, Flight
from .factories import UserFactory, FlightFactory
import json
from datetime import date

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

class GetFlightsCase(TestCase):
    def setUp(self):
        global user_1, user_2, user_3, flight_1, flight_2, flight_3

        user_1 = User.objects.create(first_name="John", last_name="Doe")
        user_2 = User.objects.create(first_name="Jane", last_name="Smith")
        user_3 = User.objects.create(first_name="Jack", last_name="Jones")

        flight_1 = Flight.objects.create(
            user=user_1,
            date=date.today(),
            start_location="JFK",
            end_location="LAX",
            day_hours=1.00,
            night_hours=0.00,
            aircraft="C172",
            description="Test flight 1.",
            role="Pilot",
        )

        flight_2 = Flight.objects.create(
            user=user_1,
            date=date.today(),
            start_location="ILM",
            end_location="DFW",
            day_hours=3.00,
            night_hours=1.50,
            aircraft="Boeing 747",
            description="Test flight 2.",
            role="Pilot",
        )

        flight_3 = Flight.objects.create(
            user=user_2,
            date=date.today(),
            start_location="PDX",
            end_location="LGA",
            day_hours=2.50,
            night_hours=0.50,
            aircraft="Boeing 737",
            description="Test flight 3.",
            role="Pilot",
        )

    def test_return_user_flights(self):
        c = Client()
        response_1 = c.get(f"/api/v1/users/{user_1.id}/flights/")
        self.assertEqual(response_1.status_code, 200)

        data = json.loads(response_1.content)["data"]

        self.assertEqual(len(data), 2)
        flight_response_1 = data[0]
        flight_response_2 = data[1]

        self.assertEqual(flight_response_1["id"], f"{flight_1.id}")
        self.assertEqual(flight_response_2["id"], f"{flight_2.id}")

        self.assertEqual(flight_response_1["type"], "flight")
        self.assertEqual(flight_response_2["type"], "flight")

        attributes = flight_response_1["attributes"]
        self.assertEqual(attributes["date"], flight_1.date.isoformat())
        self.assertEqual(attributes["start_location"], flight_1.start_location)
        self.assertEqual(attributes["end_location"], flight_1.end_location)
        self.assertEqual(attributes["day_hours"], flight_1.day_hours)
        self.assertEqual(attributes["night_hours"], flight_1.night_hours)
        self.assertEqual(attributes["aircraft"], flight_1.aircraft)
        self.assertEqual(attributes["description"], flight_1.description)
        self.assertEqual(attributes["role"], flight_1.role)
        self.assertNotIn("user", attributes)

        response_2 = c.get(f"/api/v1/users/{user_2.id}/flights/")
        self.assertEqual(response_2.status_code, 200)

        data = json.loads(response_2.content)["data"]

        self.assertEqual(len(data), 1)
        flight_response_3 = data[0]

        self.assertEqual(flight_response_3["id"], f"{flight_3.id}")
        self.assertEqual(flight_response_3["type"], "flight")

    def test_return_empty_array_if_user_has_no_flights(self):
        c = Client()
        response = c.get(f"/api/v1/users/{user_3.id}/flights/")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)["data"]
        self.assertEqual(len(data), 0)
        self.assertEqual(data, [])

    def test_return_error_if_user_not_found(self):
        c = Client()
        response = c.get(f"/api/v1/users/100/flights/")
        self.assertEqual(response.status_code, 404)
        error = json.loads(response.content)["errors"][0]["detail"]
        self.assertEqual(error, "Invalid user id.")

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
            'role': 'Pilot',
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
                                    'end_location': ['This field is required.'],
                                    'role': ['This field is required.']}
                                ]
                            }
        self.assertEqual(response.json(), expected_response)
        
        self.assertFalse(Flight.objects.filter(user=user).exists())
