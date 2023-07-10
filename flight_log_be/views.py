from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from copy import deepcopy

from .serializers import FlightSerializer
from .models import User

@api_view(['POST'])
def create_flight(request, user):
  data = deepcopy(request.data)
  data['user'] = user
  serializer = FlightSerializer(data=data)
  
  if serializer.is_valid():
    serializer.save()
    flight_data = {"data": 
                    {"type": "flight",
                     "attributes": serializer.data
                    }
                  }
    return Response(flight_data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)