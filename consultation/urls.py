from django.urls import path
from .views import (
    consultation_detail,
    doctor_consultation_list,
    user_consultation_list,
    create_consultation,
    answer_consultation, 
    )
urlpatterns = [
    path('answer/<int:pk>/', answer_consultation, name='answer_consultation'),
    path("create/", create_consultation, name="create_consultation"),
    path("user/", user_consultation_list, name="user_consultation_list"),
    path("doctor/", doctor_consultation_list, name="doctor_consultation_list"),
    path("<int:pk>/", consultation_detail, name="consultion_detail"),
]