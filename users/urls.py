from django.urls import path
from .views import homeView, userCreateView, userLoginView, Logout, userProfile


urlpatterns = [
    path('user/profile', userProfile, name='user_profile'),
    path('logout/', Logout, name="logout"),
    path("login/user/", userLoginView, name="login" ),
    path("user/create", userCreateView, name="user_create"),
    path("", homeView, name="home"),
]