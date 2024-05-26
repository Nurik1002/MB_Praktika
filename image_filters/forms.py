from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile

class ImageUploadForm(forms.Form):
    image = forms.ImageField()