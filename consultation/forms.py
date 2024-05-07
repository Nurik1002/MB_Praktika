from django import forms

from .models import Consultation, ConsultationAnswer
from user.models import CustomUser, Doctor


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['title',  'description', 'doctor']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id':'titleid'}),
            # 'photo': forms.FileInput(attrs={'class': 'form-control'}),
            # 'files': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id':'descriptionid'}),
            'doctor': forms.Select(attrs={'class': 'form-control', 'id':'doctors'}),
        }


class ConsultationAnswerForm(forms.ModelForm):
    class Meta:
        model = ConsultationAnswer
        fields = ['diagnosis', 'recommendation']
        widgets = {
            'diagnosis': forms.TextInput(attrs={'class': 'form-control', 'id':'diagnosisid'}),
            'recommendation': forms.Textarea(attrs={'class': 'form-control', 'id':'recommendationid'}),
        }