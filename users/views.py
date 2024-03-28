from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def homeView(request):
    return  render(request, "home.html", {})