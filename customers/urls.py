from django.urls import path
from customers import views

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path("dashboard/", views.DashboardView.as_view(), name='dashboard'),
    path("add-new-advertisement-site/", views.AddNewAdvertisementSiteView.as_view(), name='add_new_advertisement_site'),
    path("modify-existing-advertisement-site/", views.MOdifyExistingAdvertisementSiteView.as_view(), name='modify_existing_advertisement_site'),
    path("create-booking", views.CreateBookingView.as_view(), name='create_booking'),
    path("see-all-booking", views.SeeAllBookingView.as_view(), name='see_all_booking'),
    path("dashboard-invoice", views.DashboardInvoiceView.as_view(), name='dashboard_invoice'),




]
