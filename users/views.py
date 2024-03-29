from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Administrator, User, Doctor
from .forms import AdminCreationForm, DoctorCrteationForm, UserCreationForm


# class AdministratorCreateView(CreateView):
#     form_class = AdminCreationForm
#     template_name = 'create_administrator.html'
#     success_url = reverse_lazy('success') 

    
def homeView(request):
    return  render(request, "home.html", {})


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('home') 
    