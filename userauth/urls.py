from django.urls import path
from userauth import views

urlpatterns = [
    path("register/", views.RegisterWithOtpView.as_view(), name='register'),
    path("send-otp/", views.send_otp, name='send_otp'),
    path("about-us/", views.AboutView.as_view(), name='about_us'),
    path("contact-us/", views.ContactView.as_view(), name='contact_us'),
    path("circulars/", views.CircularsView.as_view(), name='circulars'),
    path("term-and-conditions/", views.TermAndConditionsView.as_view(), name='term_and_conditions'),
    path("property-grid/", views.PropertyGridView.as_view(), name='property_grid'),
    path("property-single/", views.propertySingleView.as_view(), name='property_single'),
    path("blog-grid/", views.BlogGridView.as_view(), name='blog_grid'),
    path("blog-single/", views.BlogSingleView.as_view(), name='blog_single'),
    path("agent-grid/", views.AgentGridView.as_view(), name='agent_grid'),
    path("agent-single/", views.AgentSingleView.as_view(), name='agent_single'),
    path("sites/", views.SiteView.as_view(), name='sites'),
    path("booking/", views.BookingView.as_view(), name='booking'),
    path("invoices/", views.InvoicesView.as_view(), name='invoices'),
    path("property-search-grid/", views.PropertySearchGrid.as_view(), name='property_search_grid'),

    path("user-register-profile/", views.UserRegisterProfile.as_view(), name='user_register_profile'),
    path("user-business-register-profile/", views.UserBusinessProfile.as_view(), name='user_business_profile'),
    path("user-update-profile/", views.UserUpdateProfile.as_view(), name='user_update_profile'),

    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogOutView.as_view(), name='logout'),
]
