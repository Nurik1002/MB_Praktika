from django.urls import path
from ..app.views import homeView, userCreateView, userLoginView, Logout
urlpatterns = [
    path('logout/', Logout, name="logout"),
    path("login/user/", userLoginView, name="login" ),
    path("create/user/", userCreateView, name="user_create"),
    path("", homeView, name="home"),
]