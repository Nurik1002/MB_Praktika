from django.urls import path

from .views import (
    post_create,
    post_detail,

    
)

urlpatterns = [
    path('<int:pk>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
]