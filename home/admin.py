from django.contrib import admin
from .models import Notification, Timetable

# Register your models here.
admin.site.register((Notification, Timetable ))
