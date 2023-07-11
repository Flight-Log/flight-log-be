from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

def user_list(request):
  
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return JsonResponse(serializer.data, safe=False)


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
