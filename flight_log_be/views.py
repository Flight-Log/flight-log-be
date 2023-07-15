from django.http import JsonResponse
from .models import User, Flight
from .serializers import UserSerializer, FlightSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from copy import deepcopy

# from rest_framework.views import APIView --> needed for class-based views if using JSON-API


@api_view(["GET"])
def return_a_user(request, id):
    try:
        user = User.find_user(id)
    except:
        return JsonResponse(User.error_404(), status=404)
    serializer = UserSerializer(user)
    return JsonResponse(User.serialize_user(serializer, user.id), status=200)


def return_users(request):
    users = User.all_users()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(User.serialize_users(users, serializer), status=200)


@api_view(["GET", "POST"])
def return_flights(request, user):
    if request.method == "GET":
        try:
            found_user = User.find_user(user)
        except:
            return JsonResponse(User.flight_error_404(), status=404)

        flights = Flight.find_flights(found_user)
        serializer = FlightSerializer(flights, many=True)
        return JsonResponse(Flight.serialize_flights(flights, serializer), status=200)

    elif request.method == "POST":
        data = deepcopy(request.data)
        data["user"] = user
        serializer = FlightSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(Flight.serialize_flight(serializer), status=status.HTTP_201_CREATED)

        else:
            return Response(Flight.error_400(serializer), status=status.HTTP_400_BAD_REQUEST)


# Class-based view for using JSON-API approach to serialization

# class FlightList(APIView):
#     resource_name = "flight"

#     def get(self, request, id):
#         try:
#             user = User.objects.get(pk=id)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         flights = Flight.objects.filter(user=user)
#         serializer = FlightSerializer(flights, many=True)
#         return Response(serializer.data)
