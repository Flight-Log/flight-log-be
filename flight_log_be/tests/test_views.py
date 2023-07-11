from django.test import TestCase
from flight_log_be.models import User
from flight_log_be.models import Flight
from django.test import Client
import json
from datetime import date


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
            day_hours=1.0,
            night_hours=0.0,
            aircraft="C172",
            description="Test flight 1.",
            role="Pilot",
        )

        flight_2 = Flight.objects.create(
            user=user_1,
            date=date.today(),
            start_location="ILM",
            end_location="DFW",
            day_hours=3.0,
            night_hours=1.5,
            aircraft="Boeing 747",
            description="Test flight 2.",
            role="Pilot",
        )

        flight_3 = Flight.objects.create(
            user=user_2,
            date=date.today(),
            start_location="PDX",
            end_location="LGA",
            day_hours=2.5,
            night_hours=0.5,
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
