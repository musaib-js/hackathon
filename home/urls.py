from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('timetable/', views.timetable, name = "timetable"),
    path('noticeboard/', views.noticeboard, name = "noticeboard"),
    path('signup/', views.signup, name = "Signup"),
    path('login/', views.handleLogin, name= "login"),
    path('logout/', views.handleLogout, name= "logout"),
    path('profile/', views.profile, name = "profile"),
    path('<str:slug>/', views.notice, name = "notice"),
    
]
