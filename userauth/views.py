from django.shortcuts import render
from django.views.generic import View

class LoginView(View):
    template_name = "userauth/login.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass