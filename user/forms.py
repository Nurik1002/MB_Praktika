from .models import CustomUser
from django import forms

from django.contrib import admin

class EditCustomUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name', 'photo', 'phone_number']