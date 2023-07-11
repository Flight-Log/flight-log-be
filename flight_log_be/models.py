from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Flight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(max_length=50)
    start_location = models.CharField(max_length=50)
    end_location = models.CharField(max_length=50)
    day_hours = models.FloatField(max_length=50)
    night_hours = models.FloatField(max_length=50)
    aircraft = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    role = models.CharField(max_length=50)

    def __str__(self):
        return str(self.start_location + " to " + self.end_location)
