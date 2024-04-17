from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Consultation, MyChat, PrivateChat, GroupChat, Message, Doctor, CustomUser


@login_required(login_url='login')
def consultatoinFilterByDoctor(request, pk):
    if request.method == 'GET':
        user = CustomUser.objects.get(id=pk)
        doctor = Doctor.objects.get(user=user)
        if doctor:

            consultations = Consultation.objects.filter(doctor_id=doctor.id)
            consultation_data = [  
                {
                "id" : constation.id,
                "title" : constation.title,
                "description" : constation.description,
                "user_id" : constation.user_id,
                }
                for constation in consultations
            ]
            return JsonResponse({"consultations": consultation_data}, status=200)
        else:
            return JsonResponse({"error": "Missing doctor id" }, status=400)
    else:
        return JsonResponse({"error": "Invalid request" }, status=400)
    



@login_required(login_url='login')
def consultation(request, pk):
    user = CustomUser.objects.get(id=pk)
    doctor = Doctor.objects.get(user=user)
    return render(request, "doctor/consultations.html", {"doctor": doctor})