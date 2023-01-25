from django.shortcuts import render
from django.views.generic import View


class HomePage(View):
    def get(self, request):
        template = 'customers/index.html'
        print("The current user =====",request.user)
        return render(request, template)


