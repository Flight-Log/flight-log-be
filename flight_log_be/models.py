from django.db import models
from django.utils import timezone

class User(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
    return str(self.first_name + " " + self.last_name)

class Flight(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_flights')
  date = models.DateField(default=timezone.now)
  start_location = models.CharField(max_length=50)
  end_location = models.CharField(max_length=50)
  day_hours = models.DecimalField(max_digits=4, decimal_places=2)
  night_hours = models.DecimalField(max_digits=4, decimal_places=2)
  aircraft = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  role = models.CharField(max_length=50)

  def __str__(self):
    return '{} to {}'.format(self.start_location, self.end_location)