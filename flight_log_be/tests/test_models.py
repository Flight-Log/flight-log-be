from django.test import TestCase
from flight_log_be.models import User
from flight_log_be.models import Flight
from datetime import date


class UserTest(TestCase):
    def setUp(self):
        User.objects.create(first_name="John", last_name="Doe")
        User.objects.create(first_name="Jane", last_name="Smith")

    def test_user_last_name(self):
        john = User.objects.get(first_name="John")
        jane = User.objects.get(first_name="Jane")
        self.assertEqual(john.last_name, "Doe")
        self.assertEqual(jane.last_name, "Smith")


class FlightTest(TestCase):
    def setUp(self):
        User.objects.create(first_name="John", last_name="Doe")
        Flight.objects.create(
            user=User.objects.get(first_name="John"),
            date=date.today(),
            start_location="JFK",
            end_location="LAX",
            day_hours=1.0,
            night_hours=0.0,
            aircraft="C172",
            description="Test flight.",
            role="Pilot",
        )

    def test_flights(self):
        flight = Flight.objects.get(start_location="JFK")
        self.assertEqual(flight.date, date.today())
        self.assertEqual(flight.end_location, "LAX")
        self.assertEqual(flight.day_hours, 1.0)
        self.assertEqual(flight.night_hours, 0.0)
        self.assertEqual(flight.aircraft, "C172")
        self.assertEqual(flight.description, "Test flight.")
        self.assertEqual(flight.role, "Pilot")
