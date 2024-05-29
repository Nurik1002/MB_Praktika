from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Consultation, ConsultationAnswer
from .forms import ConsultationForm, ConsultationAnswerForm
from user.models import CustomUser, Doctor

@login_required(login_url='login')
def doctor_consultation_list(request):
    context = dict()
    doctor = Doctor.objects.get(user = request.user)
    context['consultations'] = Consultation.objects.filter(doctor=doctor)
    return render(request, "consultations/doctor_consultation_list.html", context=context)


@login_required(login_url='login')
def user_consultation_list(request):
    context = dict()
    context['consultations'] = Consultation.objects.filter(user=request.user)
    return render(request, "consultations/consultation_list.html", context=context)

@login_required(login_url='login')
def consultation_detail(request, pk):
    context = dict()
    consultation = Consultation.objects.get(id=pk)
    context['consultations'] = consultation
    answers = ConsultationAnswer.objects.filter(consultation=consultation)
    context['answers'] = answers
    return render(request, "consultations/consultation_detail.html", context=context)


@login_required(login_url='login')
def create_consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST, request.FILES)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.user = request.user
            consultation.save()
            return redirect('user_consultation_list')
            # return JsonResponse({'success': True})
    else:
        form = ConsultationForm()
    return render(request, "consultations/consultation_form.html", {'form': form})


@login_required(login_url='login')
def answer_consultation(request, pk):
    if request.method == 'POST':
        form = ConsultationAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            consultation = Consultation.objects.get(id=pk)
            answer.consultation = consultation
            doctor = Doctor.objects.get(user = request.user)
            answer.doctor=doctor
            answer.save()
            return redirect(doctor_consultation_list)
            #
    else:
        form = ConsultationAnswerForm()
        consultation = Consultation.objects.get(id=pk)
    return render(request, "consultations/consultation_answer_form.html", {'form': form, 'consultation':consultation })