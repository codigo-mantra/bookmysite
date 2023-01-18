from django.urls import path
from customers import views

urlpatterns = [
    path("", views.HomePage.as_view(), name='home')
]
