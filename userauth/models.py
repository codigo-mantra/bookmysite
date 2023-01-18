from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        # if not email:
        #     # raise ValueError(_("The Email must be set !"))
        #     email = "_@gmail.com"
        # else:
        #     email = "_@gmail.com"
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **extra_fields)

class TimeStampModel(models.Model):
    """TimeStamp Model"""
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now, editable=False)


class User(AbstractBaseUser, TimeStampModel):
    """User Model"""
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

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
        
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return "{}".format(self.phone_number)

