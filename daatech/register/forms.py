from django import forms 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

USER_TYPES = [
        ("SME", "SMEs"),
        ("Insurance", "Insurance Company"),
        ("Commercial", "Commercial Bank"),
        ("Microfinance", "Microfinance Institution")
    ]

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    user_type = forms.ChoiceField(choices=USER_TYPES)


    
    class Meta:
        model = User
        fields = ["username","first_name","last_name", "email", "password1", "password2"]