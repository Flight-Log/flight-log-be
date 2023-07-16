from django.contrib import admin
from .models import User
from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    ordering = ['id']
    
admin.site.register(User)
admin.site.register(Flight)