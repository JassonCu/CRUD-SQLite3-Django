from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

class UserAccountCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
