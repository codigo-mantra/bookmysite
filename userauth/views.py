from django.views.generic import View, TemplateView
from django.http import JsonResponse
import random, boto3
from django.shortcuts import render, redirect, HttpResponseRedirect
import random
from .models import Otp, User
from django.contrib.auth import authenticate, login, logout
from .forms import PersonRegisterForm, UserBusinessProfileForm
from django.urls import reverse

class UserRegisterProfile(View):

    def get(self, request):
        template = 'authentication/register-user-profile.html'
        phone_number = request.session.get('phone_number')
        return render(request,template,{'phone_number':phone_number})

    def post(self, request):
        form = PersonRegisterForm(request.POST or None)
        phone_number = request.session.get('phone_number')
        if form.is_valid():
            userprofile = form.save(commit=False)
            password = form.cleaned_data.get('password')
            userprofile.username = phone_number
            userprofile.phone_number = phone_number
            userprofile.save()
            user = authenticate(username=userprofile.username, password=password)
            if user is not None and user.check_password(password):
                login(request, user)
                return HttpResponseRedirect(reverse("user_business_profile"))
            else:
                return HttpResponseRedirect(reverse("user_register_profile"))
        else:
            return HttpResponseRedirect(reverse("user_register_profile"))

class LogOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("home"))

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
        is_registerd = False
        is_otp_verified = False
        data = {}
        phone_number = request.POST.get("phone_number")
        otp_obj = Otp.objects.filter(phone_number=phone_number).first()
        if otp_obj:
            if otp_obj.is_verified:
                is_otp_verified = True
        else:
            gen_otp = random.randint(100000, 999999)
            message = f"This is ONE TIME PASSWORD - {gen_otp}"
            SendOtp = PhoneConfirmation()
            SendOtp.publish(phone_number, message)
            Otp.objects.update_or_create(phone_number=phone_number, defaults={'otp': gen_otp})
        if User.objects.filter(phone_number=phone_number).exists():
            is_registerd = True
            is_otp_verified = True
            # return JsonResponse(data,status=200)
        data['is_registerd'] = is_registerd
        data['is_otp_verified'] = is_otp_verified
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({"message": "Not send"}, status=400)

# def dashboard(request):
#     template = 'authentication/register-user-profile.html'
#     phone_number = request.session.get('phone_number')
#     return render(request,template,{'phone_number':phone_number})



class LoginView(View):
    def post(self,request):
        is_logged_in = False
        print(request.POST, "################")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None and user.check_password(password):
            login(request, user)
            is_logged_in = True
            print("User logged in successfully and Return True!")
            return JsonResponse({"is_logged_in": is_logged_in}, status=200)
        else:
            print("Failed user login and Return False!")
            return JsonResponse({"is_logged_in": is_logged_in}, status=200)



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

class SiteView(View):
    def get(self,request):
        context = {}
        template = 'customers/sites.html'
        return render(request, template, context)


class CircularsView(View):
    def get(self,request):
        context = {}
        template = 'customers/circulars.html'
        return render(request, template, context)


class TermAndConditionsView(View):
    def get(self,request):
        template = 'customers/term_conditions.html'
        return render(request, template)

class PropertyGridView(View):
    def get(self,request):
        template = 'customers/property-grid.html'
        return render(request, template)

class propertySingleView(View):
    def get(self,request):
        template = 'customers/property-single.html'
        return render(request, template)

class BlogGridView(View):
    def get(self,request):
        template = 'customers/blog-grid.html'
        return render(request, template)

class BlogSingleView(View):
    def get(self,request):
        template = 'customers/blog-single.html'
        return render(request, template)

class AgentGridView(View):
    def get(self,request):
        template = 'customers/agents-grid.html'
        return render(request, template)


class AgentSingleView(View):
    def get(self,request):
        template = 'customers/agent-single.html'
        return render(request, template)





class UserBusinessProfile(View):
    def get(self,request):
        template = 'authentication/register-user-business.html'
        print(request.user, "&&&&&&&&&&&&&&&&&&&&&&&&&")
        user_id = request.user.pk
        return render(request,template, {'user_id': user_id})
    def post(self, request):
        form = UserBusinessProfileForm(request.POST or None)
        if form.is_valid():
            user_profile = request.user.pk
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse("user_business_profile"))
        
