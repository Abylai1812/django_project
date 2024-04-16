from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Parent

class LoginForm(AuthenticationForm):
    pass

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Parent
        fields = ['iin', 'first_name', 'last_name', 'password', 'phone', 'address']