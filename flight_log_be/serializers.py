from rest_framework import serializers
from .models import User
from .models import Flight


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            "id",
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
