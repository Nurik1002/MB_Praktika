from django.urls import path
from .views import (
    consultatoinFilterByDoctor, 
    consultationFilterByUser,
    create_consultation,
    get_all_doctors,
)

urlpatterns = [
    path("get/doctors/", get_all_doctors, name="get_all_doctors"),
    path('create/consultation/', create_consultation, name='ajaxcreateConsultation'),
    path("<int:pk>/filter/consultations/by/user/", consultationFilterByUser, name="filterConsultationByUser"),
    path('<int:pk>/filter/consultations/by/doctor/', consultatoinFilterByDoctor, name='filterConsultations'),
]