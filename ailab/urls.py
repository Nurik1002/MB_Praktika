from django.urls import path
from .views import brain_view

urlpatterns = [
    path("brain/tumors/", brain_view, name="braun_tumoes"),
]