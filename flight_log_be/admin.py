from django.contrib import admin
from .models import User
from .models import Flight

admin.site.register(User)
admin.site.register(Flight)

class Flight(admin.Flight):
    id = "id"