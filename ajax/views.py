from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from consultation.models import Consultation, ConsultationAnswer
from user.models import CustomUser, Doctor
from consultation.forms import ConsultationForm, ConsultationAnswerForm







@login_required(login_url='login')
def get_all_doctors(request):
    if request.method == 'GET':
        docors = Doctor.objects.all()
        if docors:
            data = [
                {
                    "doctor_id" : doctor.id,
                    "doctor_spec" : doctor.specialist,
                    "doctor_fullname" : doctor.user.last_name + " " + doctor.user.first_name,    
                }
            for doctor in docors
            ]
            return JsonResponse({"data": data})
        else:
            return JsonResponse({"error": "Doctors not exist"})
    else:
        return JsonResponse({'error': 'Invalid request method.'})


# @login_required(login_url='login')
# def consultatoinFilterByDoctor(request, pk):
#     if request.method == 'GET':
#         user = CustomUser.objects.get(id=pk)
#         doctor = Doctor.objects.get(user=user)
#         if doctor:

#             consultations = Consultation.objects.filter(doctor_id=doctor.id)
#             consultation_data = [  
#                 {
#                 "id" : constation.id,
#                 "title" : constation.title,
#                 "description" : constation.description,
#                 "user_id" : constation.user_id,
#                 }
#                 for constation in consultations
#             ]
#             return JsonResponse({"consultations": consultation_data}, status=200)
#         else:
#             return JsonResponse({"error": "Missing doctor id" }, status=400)
#     else:
#         return JsonResponse({"error": "Invalid request" }, status=400)
    

# @login_required(login_url='login')
# def consultationFilterByUser(request, pk):
#     if request.method == "GET":
#         user  = CustomUser.objects.get(id=pk)
#         if user:
#             consultations = Consultation.objects.filter(user=user)
#             consultation_data = [
#                 {
#                 "id" : constation.id,
#                 "title" : constation.title,
#                 "description" : constation.description,
#                 "user_id" : constation.user_id,
#                 "doctor_id" : constation.doctor_id
#                 }
#                 for constation in consultations
#             ]
#             return JsonResponse({"consultations": consultation_data}, status=200)
#         else:
#             return JsonResponse({"error": "Missing doctor id" }, status=400)
#     else:
#         return JsonResponse({"error": "Invalid request" }, status=400)
