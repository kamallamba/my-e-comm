from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.contrib.auth.models import User
from .models import Customer,Cart

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=70,
        widget=forms.TextInput(attrs={"autofocus": "True", 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','mobile','zipcode','state']


