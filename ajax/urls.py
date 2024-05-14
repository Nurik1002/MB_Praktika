from django.urls import path
from .views import (

    get_all_doctors,

)

urlpatterns = [

    path("get/doctors/", get_all_doctors, name="get_all_doctors"),


]