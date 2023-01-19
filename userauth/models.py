from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html

# class UserManager(BaseUserManager):
    # def create_user(self, username, password, **extra_fields):
    #     # if not email:
    #     #     # raise ValueError(_("The Email must be set !"))
    #     #     email = "_@gmail.com"
    #     # else:
    #     #     email = "_@gmail.com"
    #     # email = self.normalize_email(email)
    #     user = self.model(username=username, **extra_fields)
    #     user.set_password(password)
    #     user.save()
    #     return user
    # def create_superuser(self, username, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     extra_fields.setdefault('is_active', True)

    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError(_("Superuser must have is_staff=True."))
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError(_("Superuser must have is_superuser=True."))
        # return self.create_user(username, password, **extra_fields)

class TimeStampModel(models.Model):
    """TimeStamp Model"""
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now, editable=False)


# class User(AbstractBaseUser, TimeStampModel):
#     """User Model"""
#     username = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(_('email address'), null=True, blank=True)
#     gender = models.CharField(max_length=10)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

    # def get_full_name(self):
    #     return f"{self.first_name} {self.last_name}"

    # def get_short_name(self):
    #     return f"{self.first_name}"

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True
        
    # class Meta:
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'

    # def __str__(self):
    #     return "{}".format(self.phone_number)


# class UserManager(BaseUserManager):
#     def create_user(self, phone_number, password, gender, **extra_fields):
#         user = self.model(phone_number=phone_number, gender=gender, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, phone_number, password, gender, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError(_("Superuser must have is_staff=True."))
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError(_("Superuser must have is_superuser=True."))
#         return self.create_user(phone_number, password, gender, **extra_fields)


# class User(AbstractBaseUser):
#     """User Model"""
#     username = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(_('email address'), null=True, blank=True)
#     phone_number = models.CharField(max_length=15, unique=True)
#     gender = models.CharField(max_length=10)
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = ['gender']
#     objects = UserManager()

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def __str__(self):
#         return "{}".format(self.phone_number)



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
