from django.urls import path
from .views import (
    homeView, 
    userCreateView, 
    userLoginView, 
    Logout, 
    userProfile, 
    createDoctor,
    )


urlpatterns = [
    path('doctor/create/', createDoctor, name='create_doctor'),
    path('user/profile/', userProfile, name='user_profile'),
    path('logout/', Logout, name="logout"),
    path("login/user/", userLoginView, name="login" ),
    path("user/create", userCreateView, name="user_create"),
    path("", homeView, name="home"),
]