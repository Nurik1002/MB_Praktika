from django.urls import path
from .views import (
    consultatoinFilterByDoctor, 
    consultationFilterByUser,
    get_all_doctors,
    create_consultetion, 
)

urlpatterns = [
    path("get/doctors/", get_all_doctors, name="get_all_doctors"),
    path('create/consultation/', create_consultetion, name='ajaxcreateConsultation'),
    path("<int:pk>/filter/consultations/by/user/", consultationFilterByUser, name="filterConsultationByUser"),
    path('<int:pk>/filter/consultations/by/doctor/', consultatoinFilterByDoctor, name='filterConsultations'),
]