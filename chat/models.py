from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now
from django.urls import reverse

from user.models import CustomUser, Doctoryy

class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey('GroupChat', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_read_time = models.DateTimeField(default=now) 

    def __str__(self):
        return f"{self.user.username} in {self.group.name if self.group else 'Private'}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.text[:20]}..."

    class Meta:
        ordering = ['created_at']


class GroupChat(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(CustomUser)
    type = models.CharField(max_length=20, choices=[
        ('doctors', 'Doctors'),
        ('admins', 'Administrators'),
        ('all', 'All Users'),
    ])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chat:group-detail', kwargs={'pk': self.pk})

    def get_last_message(self):
        """Get the last message in this group."""
        try:
            return self.message_set.latest('created_at')
        except Message.DoesNotExist:
            return None

    def get_unread_count(self, user):
        """Get the number of unread messages for a user in this group."""
        last_read_time = user.chat_set.filter(group=self).first().last_read_time
        return self.message_set.filter(created_at__gt=last_read_time).count()