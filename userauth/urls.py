from django.urls import path
from userauth import views

urlpatterns = [
    path("register/", views.RegisterWithOtpView.as_view(), name='register' ),
    path("send-otp/", views.send_otp, name='send_otp' ),
]
