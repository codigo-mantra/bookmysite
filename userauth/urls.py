from django.urls import path
from userauth import views

urlpatterns = [
    path("register/", views.RegisterWithOtpView.as_view(), name='register'),
    path("send-otp/", views.send_otp, name='send_otp'),
    path("about-us/", views.AboutView.as_view(), name='about_us'),
    path("contact-us/", views.ContactView.as_view(), name='contact_us'),
]
