from django.contrib import admin
from .models import Notification, Timetable, todoList, classRep

# Register your models here.
admin.site.register((Notification, Timetable, todoList, classRep ))
