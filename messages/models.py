from django.db import models
from ..users.models import CustomUser, Doctor


class Consultation(models.Model):
    title = models.CharField(max_length=500, verbose_name="Title")
    photo = models.ImageField(upload_to="consultation", verbose_name="Photo")
    files = models.FileField(upload_to="files", verbose_name="Files")
    description = models.TextField(verbose_name="Description")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Patient")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor")


    def __str__(self):
        return self.title



class PrivateChat(models.Model):
    participant_1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Participant 1")
    participant_2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Participant 2")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return f"{self.participant_1.username} - {self.participant_2.username}"


class Chat(models.Model):
    name = models.CharField(max_length=500, blank=True, null=False  verbose_name="Name")
    participant = models.ManyToManyField(CustomUser, verbose_name="Participant")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return f"{self.name}"
    


class Message(models.Model):
    chat_id  
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Sender")
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    is_read = models.BooleanField(default=False, verbose_name="Is read")

