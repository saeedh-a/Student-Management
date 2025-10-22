from django.contrib.auth.models import User
from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

class StudentForm(forms.ModelForm):
    class Meta:
         model=Student
         fields=['name' , 'age' , 'course' , 'email']


class UserRegistrationForm(UserCreationForm):
     email=forms.EmailField
     class Meta:
          model=User
          fields=['username', 'email', 'password']

class UserLoginForm(AuthenticationForm):
     class Meta:
          model=User
          fields=['username',  'password']