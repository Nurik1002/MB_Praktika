from django.urls import path
from .views import homeView, UserCreateView
urlpatterns = [
    path("create/user/", UserCreateView.as_view(), name="user_create"),
    path("", homeView, name="home"),
]