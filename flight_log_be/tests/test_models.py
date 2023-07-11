from django.test import TestCase
from flight_log_be.models import User

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