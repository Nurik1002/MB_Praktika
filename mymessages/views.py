from django.shortcuts import render


from .models import Consultation, MyChat, PrivateChat, GroupChat, Message


def consultatoinFilterByDoctor(request):
    if request.method == 'GET' and request.is_ajax():
        doctor_id = request.GET.get('doctor_id')

        if doctor_id:

            consultations = Consultation.objects.filter(doctor_id=doctor_id)
            consultation_data = [  
                {
                "id" : constation.id,
                "title" : constation.title
                "description" : constation.description
                "user_id" : constation.user_id
                }
                for constation in consultations
            ]
            return JsonResponse({"consultations": consultation_data}, status=200)
        else:
            return JsonResponse({"error": "Missing doctor id" }, status=400)
    else:
        return JsonResponse({"error": "Invalid request" }, status=400)