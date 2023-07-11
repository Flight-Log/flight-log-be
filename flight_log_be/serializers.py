# from rest_framework_json_api import serializers --> configuration statement if using JSON-API
# from rest_framework_json_api.relations import ResourceRelatedField
from rest_framework import serializers
from .models import User
from .models import Flight

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            "user",
            "date",
            "start_location",
            "end_location",
            "day_hours",
            "night_hours",
            "aircraft",
            "description",
            "role",
        ]
