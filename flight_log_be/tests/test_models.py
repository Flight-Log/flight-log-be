from django.test import TestCase
from django.utils import timezone
from flight_log_be.models import User, Flight

class FlightModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='John', last_name='Doe')
        self.flight = Flight.objects.create(
            user=self.user,
            date=timezone.now().date(),
            start_location='City A',
            end_location='City B',
            day_hours=8.5,
            night_hours=2.5,
            aircraft='Boeing 747',
            description='Flight from City A to City B.',
            role='Pilot'
        )
    
    def test_flight_model_representation(self):
        self.assertEqual(
            str(self.flight),
            'City A to City B'
        )

    def test_flight_model_attributes(self):
        self.assertEqual(self.flight.user, self.user)
        self.assertEqual(self.flight.date, timezone.now().date())
        self.assertEqual(self.flight.start_location, 'City A')
        self.assertEqual(self.flight.end_location, 'City B')
        self.assertEqual(self.flight.day_hours, 8.5)
        self.assertEqual(self.flight.night_hours, 2.5)
        self.assertEqual(self.flight.aircraft, 'Boeing 747')
        self.assertEqual(self.flight.description, 'Flight from City A to City B.')
        self.assertEqual(self.flight.role, 'Pilot')
        self.assertEqual(self.flight.user.first_name, 'John')
        self.assertEqual(self.flight.user.last_name, 'Doe')


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name='John', last_name='Smith')
        User.objects.create(first_name='Jane', last_name='Doe')

    def test_user_is_created(self):
        # initial test to see if user is created correctly
        john = User.objects.get(first_name='John')
        jane = User.objects.get(first_name='Jane')
        self.assertEqual(john.last_name, 'Smith')
        self.assertEqual(jane.last_name, 'Doe')
