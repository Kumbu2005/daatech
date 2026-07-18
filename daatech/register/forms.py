from django import forms 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type  = models.CharField(choices=USER_TYPE)
    class Meta:
        model = User
        fields = ["username","first_name","last_name", "email", "password1", "password2"]