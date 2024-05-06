from django.urls import path

from .views import all_posts, create_post, post_detail

urlpatterns = [
    path('all/', all_posts, name="all_posts"),
    path('create/', create_post, name="create_post"),
    path('<int:pk>/', post_detail, name="post_detail"),
]