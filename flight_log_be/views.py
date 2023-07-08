from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from .serializers import FlightSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def user_list(request):
  
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def create_flight(request, id):
  serializer = FlightSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  else :
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  return Response(serializer.data)