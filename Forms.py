from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StartUpForm(ModelForm):
    class Meta:
        model = StartUp
        fields = '__all__'
#['Name', 'email', 'password1', 'password2', 'Field', 'Email', 'Description']

        widgets = {
            "Name": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Name'}),
            "Field": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Field'}),
            "Email": forms.EmailInput(attrs={'class': 'textbox', 'placeholder': 'Email'}),
            "Description": forms.Textarea(attrs={'class': 'textbox', 'placeholder': 'Description'})
        }


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Name'}),
            "Field": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Field'}),
            "Email": forms.EmailInput(attrs={'class': 'textbox', 'placeholder': 'Email'}),
            "Query": forms.Textarea(attrs={'class': 'textbox', 'placeholder': 'Enter your query...'})
        }


class InvestorForm(ModelForm):
    class Meta:
        model = Investor
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Name'}),
            "Field": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Area of interest'}),
            "Email": forms.EmailInput(attrs={'class': 'textbox', 'placeholder': 'Email'}),

        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
