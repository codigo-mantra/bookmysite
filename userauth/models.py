from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html

class TimeStampModel(models.Model):
    """TimeStamp Model"""
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now, editable=False)


class User(AbstractUser,TimeStampModel):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class UserBusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_business_profile")
    business_name = models.CharField(max_length=50)
    business_type = models.CharField(max_length=50)
    office_address = models.CharField(max_length=100)
    office_phone_number = models.CharField(max_length=100)
    about_business = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return f"User : {self.user} > {self.business_name}"



class Otp(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    otp          = models.CharField(max_length=6, null=True, blank=True)
    is_verified  = models.BooleanField(default=False)



class SiteProperty(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='properties/')
    size = models.CharField(max_length=255)
    type = models.CharField(max_length=255)