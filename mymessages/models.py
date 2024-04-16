from django.db import models
from django.utils import  timezone
from users.models import CustomUser, Doctor



class Consultation(models.Model):
    title = models.CharField(max_length=500, verbose_name="Title")
    photo = models.ImageField(upload_to="consultation", verbose_name="Photo")
    files = models.FileField(upload_to="files", verbose_name="Files")
    description = models.TextField(verbose_name="Description")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Patient")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"


class MyChat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    
    
    class Meta:
        abstract = True
        verbose_name = "Chat"
        verbose_name_plural = "Chats"
        


class PrivateChat(MyChat):
    user_1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Sender", related_name="private_chat_user_1")
    user_2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Reciver", related_name="private_chat_user_2")

    def __str__(self):
        return f"{self.user_1.username} - {self.user_2.username}"
    
    class Meta:
        unique_together = ("user_1", "user_2")
        verbose_name = "Private Chat"
        verbose_name_plural = "Private Chats"


class GroupChat(MyChat):
    name = models.CharField(max_length=500, verbose_name="Chat name")
    participants = models.ManyToManyField(CustomUser, verbose_name="Participants")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Group Chat"
        verbose_name_plural = "Group Chats"

class ConcreteChat(MyChat):
    pass  

class Message(models.Model):
    chat = models.ForeignKey(ConcreteChat, on_delete=models.CASCADE, verbose_name="Chat", related_name='messages')
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    read = models.BooleanField(default=False, verbose_name="Read")
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Sender")

    def __str__(self):
        return f"Message from {self.sender.username} in {self.chat}"

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"