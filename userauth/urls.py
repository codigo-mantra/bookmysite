from django.urls import path
from userauth import views

urlpatterns = [
    path("register/", views.RegisterWithOtpView.as_view(), name='register'),
    path("send-otp/", views.send_otp, name='send_otp'),
    path("about-us/", views.AboutView.as_view(), name='about_us'),
    path("contact-us/", views.ContactView.as_view(), name='contact_us'),
    # path("dashboard/", views.dashboard, name='dashboard'),
    path("user-register-profile/", views.UserRegisterProfile.as_view(), name='user_register_profile'),
    path("user-business-register-profile/", views.UserBusinessProfile.as_view(), name='user_business_profile'),
    path("login-view/", views.LoginView.as_view(), name='login_view'),



]
