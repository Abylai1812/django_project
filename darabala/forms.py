from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Parent, CustomUser

# class LoginForm(AuthenticationForm):
#     pass

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'username', 'iin', 'first_name', 'last_name', 'phone', 'address']
