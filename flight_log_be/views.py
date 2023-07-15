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
        user = User.objects.get(id=id)
    except:
        error = {"errors": [{"detail": "User not found."}]}
        return JsonResponse(error, status=404)
    serializer = UserSerializer(user)
    user_details = {
        "data": {"id": f"{user.id}", "type": "user", "attributes": serializer.data}
    }
    return JsonResponse(user_details, status=200)


def return_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    user_details = []

    for index, x in enumerate(users):
        user = {
            "id": f"{x.id}",
            "type": "user",
            "attributes": serializer.data[index],
        }
        user_details.append(user)

    user_response = {"data": user_details}

    return JsonResponse(user_response, status=200)


@api_view(["GET", "POST"])
def return_flights(request, user):
    if request.method == "GET":
        try:
            found_user = User.objects.get(pk=user)
        except:
            error = {"errors": [{"detail": "Invalid user id."}]}
            return JsonResponse(error, status=404)

        flights = Flight.objects.filter(user=found_user)
        serializer = FlightSerializer(flights, many=True)
        flight_details = []

        for index, x in enumerate(flights):
            flight = {
                "id": f"{x.id}",
                "type": "flight",
                "attributes": serializer.data[index],
            }
            flight["attributes"].pop("user")
            flight_details.append(flight)

        flight_response = {"data": flight_details}

        return JsonResponse(flight_response, status=200)

    elif request.method == "POST":
        data = deepcopy(request.data)
        data["user"] = user
        serializer = FlightSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            flight_data = {
                "data": {
                    "id": Flight.objects.last().id,
                    "type": "flight",
                    "attributes": serializer.data,
                }
            }
            return Response(flight_data, status=status.HTTP_201_CREATED)
        else:
            error = {"errors": [serializer.errors]}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


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
