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
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(default='',null=True, blank=True)

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

    def __str__(self) -> str:
        return f"User : {self.user} > {self.phone_number}"



class AdvertisementSite(models.Model):
    RENT = 1
    SALE = 2
    HOUSE =3
      
    CHOICES = (
          (RENT, 'For Rent'),
          (SALE, 'For Sale'),
          (HOUSE, 'For House'),
      )

    Name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    size = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField()
    area = models.CharField(max_length=20,null=True, blank=True)
    beds = models.IntegerField()
    baths = models.IntegerField()
    garages = models.IntegerField()
    type = models.IntegerField(choices=CHOICES, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    Longitude = models.FloatField(max_length=200, null=True, blank=True)
    Lattitude = models.FloatField(max_length=200, null=True, blank=True)
    is_active  = models.BooleanField(default=False)



class PropertyImage(TimeStampModel):
    property = models.ForeignKey(AdvertisementSite,on_delete=models.CASCADE,related_name="property_image")
    image = models.ImageField(upload_to='properties/')
    is_main  = models.BooleanField(default=False)







class Complaints(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(null=True)


    def __str__(self) -> str:
        return f"User : {self.user} > {self.name}"