import factory
from django.db import models
from flight_log_be.models import User, Flight

class UserFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = User
    
  first_name = factory.Faker('first_name')
  last_name = factory.Faker('last_name')
  
class FlightFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Flight
    
  user = factory.SubFactory(UserFactory)
  date = factory.Faker('date')
  start_location = factory.Faker('city')
  end_location = factory.Faker('city')
  day_hours = factory.Faker('pyfloat', positive=True)
  night_hours = factory.Faker('pyfloat', positive=True)
  aircraft = factory.Faker('text')
  description = factory.Faker('text')
  role = factory.Faker('job')