from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from copy import deepcopy

from .serializers import FlightSerializer, UserSerializer
from .models import User, Flight

@api_view(['POST'])
def create_flight(request, user):
  data = deepcopy(request.data)
  data['user'] = user
  serializer = FlightSerializer(data=data)
  

  if serializer.is_valid():
    serializer.save()
    flight_data = {"data": 
                    {"id": Flight.objects.last().id,
                     "type": "flight",
                     "attributes": serializer.data
                    }
                  }
    return Response(flight_data, status=status.HTTP_201_CREATED)
  else:
    error = {"errors": [serializer.errors]}
    return Response(error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])

def return_a_user(request, id):
  try:
    user = User.objects.get(id=id)
  except:
    error = {"errors": [{"detail": "User not found."}]}
    return JsonResponse(error, status=404)
  serializer = UserSerializer(user)
  user_details = {"data":
                    {"id": f"{user.id}",
                    "type": "user",
                    "attributes": serializer.data
                    }
                  }
  return JsonResponse(user_details, status=200)
