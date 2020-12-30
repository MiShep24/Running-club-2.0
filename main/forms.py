from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=75, required=True)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'firstname', 'lastname', 'email', ]
