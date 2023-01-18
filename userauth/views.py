from django.shortcuts import render, redirect
from django.views.generic import View
from phonenumbers import geocoder
from django.http import JsonResponse
import random
from .models import Otp


import boto3


class PhoneConfirmation:
    response = None
    def __init__(self) -> None:
       
        # Create an SNS client
        self.client = boto3.client(
            "sns",
            aws_access_key_id="AKIA4TJTZ6C4UTRFIWE7",
            aws_secret_access_key="JlHu9yXnvrHoI1d4V2TLV5im9JQU132+rW/b2HkU",
            region_name="us-east-1"
        )
    def publish(self, PhoneNumber, Message):
        # Send your sms message.
        print(f'--------- Sending SMS to {PhoneNumber}')
        try:
            self.response = self.client.publish(
                PhoneNumber=PhoneNumber,
                # Subject='Phone Confirmation',
                Message=Message
            )
            print(f'--------- Message: {Message} was sent to{PhoneNumber} ')

        except Exception as e:
            print(e)
            self.response = {
                "ResponseMetadata":{"HTTPStatusCode":422}
            }

def send_otp(request):
    if request.method == "POST":
        SendOtp = PhoneConfirmation()
        phone_number = request.POST.get("phone_number")
        gen_otp = random.randint(100000, 999999)
        message = f"This is ONE TIME PASSWORD - {gen_otp}"
        SendOtp.publish(phone_number, message)

        otpdata = Otp.objects.create(phone_number=phone_number,otp=gen_otp)
        otpdata.save()

        return JsonResponse({"message": "Sent Successfully!"}, status=200)
    else:
        return JsonResponse({"message": "Not send"}, status=200)

def Dashboard(request):
    template = 'Dashboard.html'
    return render(request,template)


class RegisterWithOtpView(View):
    def get(self,request):
        context = {}
        template = 'authentication/register.html'
        return render(request,template)

    def post(self,request):
        otp = request.POST.get("otp")
        phone_number = request.POST.get("phn")
        otp_obj = Otp.objects.filter(phone_number=phone_number).first()
        if otp == otp_obj.otp:
            otp_obj.is_verified = True
            otp_obj.save()
            return redirect('Dashboard')
        else:
            return JsonResponse({'message':'User not found!'})
