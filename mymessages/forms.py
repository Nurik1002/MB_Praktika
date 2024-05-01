from django import forms

from .models import Consultation
from users.models import CustomUser, Doctor


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