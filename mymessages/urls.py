from django.urls import path
from .views import (
    consultatoinFilterByDoctor, 
    consultation, 
    createConsultation, 
    myDoctors, 
    consultationFilterByUser,
    
    )

urlpatterns = [
    path("<int:pk>/filter/consultations/by/user/", consultationFilterByUser, name="filterConsultationByUser"),
    path('<int:pk>/doctors/', myDoctors, name='myDoctors'),
    path('create/consultation/', createConsultation, name='createConsultation'),
    path('<int:pk>/filter/consultations/by/doctor/', consultatoinFilterByDoctor, name='filterConsultations'),
    path('<int:pk>/consultations/', consultation, name='doctorConsultations'),
]