from django.urls import path
from .views import consultatoinFilterByDoctor

urlpatterns = [
    path('<int:pk>/consultations/', consultatoinFilterByDoctor, name='doctorConsultations'),
]