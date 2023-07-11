from django.http import JsonResponse
from .models import User
from .models import Flight
from .serializers import UserSerializer
from .serializers import FlightSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from rest_framework.views import APIView --> needed for class-based views if using JSON-API


def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def get_flights_for_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except:
        error = {"errors": [{"detail": "Invalid user id."}]}
        return JsonResponse(error, status=404)

    flights = Flight.objects.filter(user=user)
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
