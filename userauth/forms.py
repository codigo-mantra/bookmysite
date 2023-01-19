from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from .models import UserBusinessProfile

User = get_user_model()

class UserBusinessProfileForm(forms.ModelForm):
    class Meta:
        model = UserBusinessProfile
        fields = ('user', 'business_name', 'business_type', 'office_address', 'office_phone_number', 'about_business')

class PersonRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(PersonRegisterForm, self).__init__(*args, **kwargs)
        attrs = {'class': 'form-control', 'required': True}
        if self.instance and self.instance.pk:
            self.fields.pop('username', None)
        for field in self.fields.values():
            field.widget.attrs = attrs

    def clean(self):
        cleaned_data = super(PersonRegisterForm, self).clean()
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        try:
            validate_email(email)
        except forms.ValidationError as e:
            raise forms.ValidationError(_("Enter a valid email address"))
        if password == "" or password == None:
            self.fields.pop('password', None)

    def save(self, commit=True):
        m = super(PersonRegisterForm, self).save(commit=False)
        m.set_password(self.cleaned_data['password'])
        if commit:
            m.save()
        return m

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password", "phone_number", "gender")

