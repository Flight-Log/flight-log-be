from django.db import models
from django.utils import timezone
# import serializers.UserSerializer

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
    
    def find_user(id):
       return User.objects.get(id=id)
    
    def all_users():
       return User.objects.all()
    
    def error_404():
       return {"errors": [{"detail": "User not found."}]}
    
    def flight_error_404():
       return {"errors": [{"detail": "Invalid user id."}]}
    
    def serialize_user(serializer, id):
       return {
        "data": {"id": f"{id}", 
                 "type": "user", 
                 "attributes": serializer.data}
        }
    
    def serialize_users(users, serializer):
      user_details = []
      for index, x in enumerate(users):
          user = {
              "id": f"{x.id}",
              "type": "user",
              "attributes": serializer.data[index],
          }
          user_details.append(user)
      return {"data": user_details}
    
class Flight(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flight_set')
  date = models.DateField(default=timezone.now, blank=False)
  start_location = models.CharField(max_length=50, blank=False)
  end_location = models.CharField(max_length=50, blank=False)
  day_hours = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
  night_hours = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
  aircraft = models.CharField(max_length=50, blank=False)
  description = models.CharField(max_length=500, blank=True)
  role = models.CharField(max_length=50, blank=False)

  def __str__(self):
    return '{} to {}'.format(self.start_location, self.end_location)

  def find_flights(user):
    return Flight.objects.filter(user=user)
  
  def serialize_flight(serializer):
     return {
              "data": {
                  "id": f"{Flight.objects.last().id}",
                  "type": "flight",
                  "attributes": serializer.data,
              }
            }
  
  def serialize_flights(flights, serializer):
    flight_details = []
    for index, x in enumerate(flights):
        flight = {
            "id": f"{x.id}",
            "type": "flight",
            "attributes": serializer.data[index],
        }
        flight["attributes"].pop("user")
        flight_details.append(flight)
    return {"data": flight_details}
  
  def error_400(serializer):
    return {"errors": [serializer.errors]}