from django import forms
import re
from django import forms
from .models import Leaderboard
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class AddForm(forms.ModelForm):
    class Meta:
        model = Leaderboard
        fields = ['name','marks']
    def clean(self):
        pass

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.EmailField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    def clean(self):
        uname = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        if  (User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists()):
            raise forms.ValidationError("Username or Email Exists")
        else:
            return self.cleaned_data

