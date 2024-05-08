from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser,   Administrator, Doctor



admin.site.register(CustomUser)
admin.site.register(Administrator)
admin.site.register(Doctor)
