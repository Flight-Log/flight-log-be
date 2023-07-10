import factory
from flight_log_be.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')