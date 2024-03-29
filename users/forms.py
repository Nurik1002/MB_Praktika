from django import forms
from .models import Administrator, Doctor, User

class AdminCreationForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = '__all__'
        
class DoctorCrteationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'password', 'email', 'phone_number', 'photo', 'country', 'city', 'address']

