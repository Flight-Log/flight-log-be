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


@api_view(["GET"])
def flight_list(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        flights = Flight.objects.filter(user=user)
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
