from django.http import JsonResponse
from .models import User
from .models import Flight
from .serializers import UserSerializer
from .serializers import FlightSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
