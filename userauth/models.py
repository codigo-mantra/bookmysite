from django.db import models


class Otp(models.Model):
    phone_number = models.CharField(max_length=15)
    otp          = models.CharField(max_length=6, null=True, blank=True)
    is_verified  = models.BooleanField(default=False)