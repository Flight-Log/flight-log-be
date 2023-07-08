from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

def user_list(request):
  
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return JsonResponse(serializer.data, safe=False)


class ListAUser(APIView):

  def get(request, id):
    user = User.objects.get(id=id)
    return Response(status=200)
