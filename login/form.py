from django import forms
from django.forms import TextInput, NumberInput

from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register

        fields = [
            'name',
            'username',
            'email',
            'password',
            'confirm_password'
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            'username',
            'password',
        ]

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
