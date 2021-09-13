from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('timetable/', views.timetable, name = "timetable"),
    path('noticeboard/', views.noticeboard, name = "noticeboard"),
    path('<str:slug>/', views.notice, name = "notice"),
]
