from django import forms
from ckeditor.fields import RichTextFormField
from .models import Consultation, ConsultationAnswer
from user.models import CustomUser, Doctor
from django.contrib import admin


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['title', 'photo', 'files',  'description', 'doctor']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id':'titleid'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'files': forms.FileInput(attrs={'class': 'form-control'}),
            'description': RichTextFormField(config_name="default"),
            'doctor': forms.Select(attrs={'class': 'form-control', 'id':'doctors'}),
        }


class ConsultationAnswerForm(forms.ModelForm):
    class Meta:
        model = ConsultationAnswer
        fields = ['diagnosis', 'recommendation']
        widgets = {
            'diagnosis': forms.TextInput(attrs={'class': 'form-control', 'id':'diagnosisid'}),
            'recommendation': RichTextFormField(config_name="default"),
        }