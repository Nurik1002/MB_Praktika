from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Administrator(AbstractUser):
    photo = models.ImageField("Photo", blank=False, null=True, upload_to="media/admin/")
    telegram_username = models.CharField("Telegram username", max_length=25, blank=True)
    phone_number = PhoneNumberField(blank=True)
    country = models.CharField("Country", max_length=100, blank=True)
    city = models.CharField("City", max_length=100, blank=True)
    address = models.TextField("Address", blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='administrators',  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='administrator_permissions', 
        blank=True,
    )
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.phone_number}"
    
    class  Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

class Doctor(AbstractUser):
    photo = models.ImageField("Photo", blank=False, null=True, upload_to="media/doctor/")
    telegram_username = models.CharField("Telegram username", max_length=25, blank=True)
    phone_number = PhoneNumberField(blank=True)
    country = models.CharField("Country", max_length=100, blank=True)
    city = models.CharField("City", max_length=100, blank=True)
    address = models.TextField("Address", blank=True)
    work_address = models.TextField("Work address", blank=True)
    specialist = models.CharField("Specialist", max_length=255, blank=True)
    is_checked_license = models.BooleanField("Is checked license", default=False, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='doctors',  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='doctor_permissions',  
        blank=True,
    )
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.phone_number}"
    
    class  Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    

class User(AbstractUser):
    photo = models.ImageField("Photo", blank=False, null=True, upload_to="media/user/")
    telegram_username = models.CharField("Telegram username", max_length=25, blank=True)
    phone_number = PhoneNumberField(blank=True)
    country = models.CharField("Country", max_length=100, blank=True)
    city = models.CharField("City", max_length=100, blank=True)
    address = models.TextField("Address", blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users', 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',  
        blank=True,
    )
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.phone_number}"
    
    class  Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
  