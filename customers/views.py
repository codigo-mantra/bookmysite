from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from userauth.models import AdvertisementSite
from userauth.forms import AdvertisementSiteForm, PropertyImageForm
from django.contrib.auth.mixins import UserPassesTestMixin



class HomePage(View):
    def get(self, request):
        template = 'customers/index.html'
        print("The current user =====",request.user)
        return render(request, template)


class AddNewAdvertisementSiteView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('home')

    def get(self,request):
        template = 'dashboard/add-new-advertisement-site.html'
        return render(request, template)

    def post(self,request):
        form = AdvertisementSiteForm(request.POST)
        if form.is_valid():
            lattitude = float(request.POST.get('Lattitude'))
            advertisement= form.save()

            property_image_form = PropertyImageForm(self.request.POST, self.request.FILES)
            if property_image_form.is_valid():
                property_image = property_image_form.save(commit=False)
                property_image.property = advertisement
                property_image.save()
                
                return HttpResponseRedirect(reverse('modify_existing_advertisement_site'))
            return HttpResponseRedirect(reverse('add_new_advertisement_site'))

        return HttpResponseRedirect(reverse('add_new_advertisement_site'))
        
            

class DashboardView(UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('home')

    def get(self,request):
        template = 'dashboard/dashboard.html'
        return render(request, template)
        

class MOdifyExistingAdvertisementSiteView(UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('home')
        
    def get(self,request):
        template = 'dashboard/modify-existing-advertisement-site.html'
        return render(request, template)


class CreateBookingView(View):
    def get(self,request):
        template = 'dashboard/create-booking.html'
        return render(request, template)
        

class SeeAllBookingView(UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('home')

    def get(self,request):
        template = 'dashboard/see-all-booking.html'
        return render(request, template)


class DashboardInvoiceView(UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('home')
        
    def get(self,request):
        template = 'dashboard/invoice.html'
        return render(request, template)


