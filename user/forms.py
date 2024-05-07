from .models import CustomUser
from django import forms


class EditCustomUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name', 'photo', 'phone_number']