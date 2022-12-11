import form as form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from bank_app1.models import District, Branch, Customer

from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password','password1']

class NewCreationForm(forms.ModelForm):
    class Meta:
     model= Customer
     fields= 'district','branch','Account_type'





