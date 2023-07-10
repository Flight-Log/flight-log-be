from django.test import TestCase, Client
from flight_log_be.models import User, Flight
from .factories import UserFactory, FlightFactory

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