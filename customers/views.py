from django.shortcuts import render
from django.views.generic import View


class HomePage(View):
    def get(self, request):
        template = 'customers/index.html'
        return render(request, template)


