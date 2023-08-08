from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserPassword


class RegitrationForm(UserCreationForm):
    # Form to create new user
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ),
    )
    password2 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'email',)

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}
            )
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        ),
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ),
    )


class UpdatePasswordsForm(forms.ModelForm):
    class Meta:
        model = UserPassword
        fields = ['id', 'username', 'password', 'application_type',
                  'website_name', 'website_url', 'application_name', 'game_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            'application_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Application Type', 'readonly': 'readonly'
            }),
            'website_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Website Name'
            }),
            'website_url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Website url'
            }),
            'application_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Application Name'
            }),
            'game_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Game Name'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        application_type = cleaned_data.get('application_type')
        application_name = cleaned_data.get('application_name')
        website_name = cleaned_data.get('website_name')
        website_url = cleaned_data.get('website_url')
        game_name = cleaned_data.get('game_name')

        if application_type == 'Website' and not website_name:
            raise ValidationError({'website_name': 'Website name is required.'})

        if application_type == 'Website' and not website_url:
            raise ValidationError({'website_url': 'Website url is required.'})

        if application_type == 'Desktop Application' and not application_name:
            raise ValidationError({'application_name': 'Application name is required.'})

        if application_type == 'Game' and not game_name:
            raise ValidationError({'game_name': 'Game name is required.'})
