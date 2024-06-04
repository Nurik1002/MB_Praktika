from django.db import models
from django.utils import  timezone
from ckeditor.fields import RichTextField
from user.models import CustomUser, Doctor

class Consultation(models.Model):
    title = models.CharField(max_length=500, verbose_name="Title")
    photo = models.ImageField(upload_to="consultation", blank=False, null=True, verbose_name="Photo")
    files = models.FileField(upload_to="files", blank=False, null=True, verbose_name="Files")
    description = RichTextField(null=True, blank=True,    config_name="default", )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Patient")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor") 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    is_answered = models.BooleanField(default=False, verbose_name="Is Answered?") 

    def __str__(self):
        return f" {self.title} {self.doctor.id} " 

    class Meta:
        verbose_name = "Consultation"
        verbose_name_plural = "1. Consultations"

class ConsultationAnswer(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, verbose_name="Consultation")
    diagnosis = models.CharField(max_length= 500, verbose_name="Diagnosis", blank=True, null=False)
    recommendation = RichTextField(null=True, blank=True,         config_name="default", )
    
    def __str__(self):
        return f" {self.consultation.title} {self.consultation.doctor.id} " 

    class Meta:
        verbose_name = "Consultation Answer"
        verbose_name_plural = "2. Consultation Answers" 