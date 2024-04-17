from django.urls import path
from .views import consultatoinFilterByDoctor, consultation

urlpatterns = [
    path('<int:pk>/filterConsultations/', consultatoinFilterByDoctor, name='filterConsultations'),
    path('<int:pk>/consultations/', consultation, name='doctorConsultations'),
]