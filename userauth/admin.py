from django.contrib import admin
from .models import Otp,UserBusinessProfile
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from rangefilter.filters import DateRangeFilter

USER = get_user_model()


@admin.register(Otp)
class OTPAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'otp', 'is_verified']
    list_filter = ('is_verified',)
    search_fields = ['phone_number']

# admin.site.register(Otp)
admin.site.register(UserBusinessProfile)
# admin.site.register(User)

@admin.register(USER)
class PersonAdmin(UserAdmin):
    """User Admin"""
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',)
        }),)
    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "phone_number",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ('is_staff', 'is_active', 'is_superuser',)

    fieldsets = (
        ("Essentials", {"fields": ("username", "password",
                                   "last_login" ,"date_joined", "modified_at")}),
        ("Personal Information", {
         "fields": ("first_name", "last_name", "email", "phone_number", )}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", 'user_permissions')}),

    )
    # inlines = []

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["date_joined", "last_login", "modified_at"]
        else:
            return []