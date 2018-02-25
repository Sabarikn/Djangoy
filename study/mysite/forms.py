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
    email = forms.CharField(
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