from django.shortcuts import render
from django.views.generic import View, TemplateView
from phonenumbers import geocoder
from django.http import JsonResponse
import random, boto3
from django.shortcuts import render, redirect
from django.views.generic import View
from phonenumbers import geocoder
from django.http import JsonResponse
import random
from .models import Otp,User
from django.contrib.auth import authenticate, login

class LoginView(View):
    template_name = "userauth/login.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass



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
        if User.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'message':'User already exists'},status=200)
        gen_otp = random.randint(100000, 999999)
        message = f"This is ONE TIME PASSWORD - {gen_otp}"
        SendOtp.publish(phone_number, message)
        obj, created = Otp.objects.update_or_create(phone_number=phone_number, defaults={'otp': gen_otp})
        return JsonResponse({"message": "Sent Successfully!"}, status=200)
    else:
        return JsonResponse({"message": "Not send"}, status=400)

# def dashboard(request):
#     template = 'authentication/register-user-profile.html'
#     phone_number = request.session.get('phone_number')
#     return render(request,template,{'phone_number':phone_number})



class LoginView(View):
    def post(self,request):
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            # return redirect('home')
        else:
            return JsonResponse({"message":"Invalid login details supplied."})



class RegisterWithOtpView(View):
    def get(self,request):
        context = {}
        template = 'authentication/register.html'
        return render(request,template)
        
    def post(self,request):
        otp = request.POST.get("otp")
        phone_number = request.POST.get("phn")
        request.session['phone_number'] = phone_number
        
        otp_obj = Otp.objects.filter(phone_number=phone_number).first()
        if otp == otp_obj.otp:
            otp_obj.is_verified = True
            otp_obj.save()
            return JsonResponse({'message':'True'},status=200)
        else:
            return JsonResponse({'message':'False'},status=400)

class AboutView(View):
    def get(self,request):
        context = {}
        template = 'customers/about.html'
        return render(request, template, context)

class ContactView(View):
    def get(self,request):
        context = {}
        template = 'customers/contact.html'
        return render(request, template, context)


class UserRegisterProfile(View):

    def get(self,request):
        template = 'authentication/register-user-profile.html'
        phone_number = request.session.get('phone_number')
        return render(request,template,{'phone_number':phone_number})

    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        user = User.objects.filter(phone_number=phone_number)
        if user.exists():
            return JsonResponse({'message':'User already exists'},status=200)
        else:
            user = User.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,gender=gender,password=password)
            return redirect('/UserBusinessProfile')





class UserBusinessProfile(View):
    def get(self,request):
        template = 'authentication/register-user-business.html'
        return render(request,template)
        
