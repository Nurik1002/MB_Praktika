from django.db import models
from ..users.models import CustomUser, Doctor


class Consultation(models.Model):
    title = models.CharField(max_length=500, verbose_name="Title")
    photo = models.ImageField(upload_to="consultation", verbose_name="Photo")
    files = models.FileField(upload_to="files", verbose_name="Files")
    description = models.TextField(verbose_name="Description")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Patient")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor")
