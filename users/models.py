from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    country = models.CharField("Country", max_length=100, blank=True)
    state = models.TextField("State",max_length=100,  blank=True)
    city = models.CharField("City", max_length=100, blank=True)
    phone_number = PhoneNumberField(blank=True)
    photo = models.ImageField(upload_to="user")
    is_doctor = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
   

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.phone_number}"

    class  Meta:
        verbose_name = 'BaseUser'
        verbose_name_plural = 'BaseUsers'



class Administrator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    telegram_username = models.CharField("Telegram username", max_length=25, blank=True)
   
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.phone_number}"
    
    class  Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    telegram_username = models.CharField("Telegram username", max_length=25, blank=True)
    work_address = models.TextField("Work address", blank=True)
    specialist = models.CharField("Specialist", max_length=255, blank=True)
    is_checked_license = models.BooleanField("Is checked license", default=False, blank=True)
    
    
    def __str__(self) -> str:
        return f"{self.user.last_name} {self.user.first_name} {self.user.phone_number}"
    
    class  Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    

