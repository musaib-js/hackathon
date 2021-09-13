from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name = 'students'),
    path('search/', views.search, name = "search"),
    path('<str:name>/', views.studentdetails, name = "studentdetails"),
    
]
