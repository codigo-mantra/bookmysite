from django.contrib import admin
from .models import Otp,UserBusinessProfile,User
# Register your models here.

admin.site.register(Otp)
admin.site.register(UserBusinessProfile)
admin.site.register(User)

