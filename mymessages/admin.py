from django.contrib import admin
from .models import Consultation, PrivateChat, GroupChat, Message


admin.site.register(Consultation)
admin.site.register(PrivateChat)
admin.site.register(GroupChat)
admin.site.register(Message)
