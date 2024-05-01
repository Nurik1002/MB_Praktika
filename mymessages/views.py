from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Consultation, MyChat, PrivateChat, GroupChat, Message, Doctor, CustomUser
from .forms import ConsultationForm
    


@login_required(login_url='login')
def consultation(request, pk):
    user = CustomUser.objects.get(id=pk)
    doctor = Doctor.objects.get(user=user)
    return render(request, "doctor/consultations.html", {"doctor": doctor})

@login_required(login_url='login')
def createConsultation(request):
    context = dict()
    context["form"] = ConsultationForm()
    return render(request, "patient/createConsultation.html", context=context)

@login_required(login_url='login')
def myDoctors(request, pk):
    user = CustomUser.objects.get(id=pk)
    return render(request, "patient/myConsultations.html", {"user": user})