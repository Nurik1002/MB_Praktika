from django.urls import path
from .views import (
    homeView, 
    userCreateView, 
    userLoginView, 
    Logout, 
    userProfile, 
    createDoctor,
    doctorHomeView, 
    )


urlpatterns = [
    path('doctor/create/', createDoctor, name='doctor_create'),
    path('user/<str:uname>/', userProfile, name='profile'),
    path('logout/', Logout, name="logout"),
    path("login/", userLoginView, name="login" ),
    path("user/create", userCreateView, name="user_create"),
    path("", homeView, name="home"),
]