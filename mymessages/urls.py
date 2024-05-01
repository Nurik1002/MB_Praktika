from django.urls import path
from .views import (
    consultation, 
    createConsultation, 
    myDoctors,     
    )

urlpatterns = [

    path('<int:pk>/doctors/', myDoctors, name='myDoctors'),
    path('create/consultation/', createConsultation, name='createConsultation'),

    path('<int:pk>/consultations/', consultation, name='doctorConsultations'),
]