from django.contrib.auth.models import User
from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

class StudentForm(forms.ModelForm):
    class Meta:
         model=Student
         fields=['name' , 'phone' , 'department' , 'email']
         widgets= {
              'name':forms.TextInput(attrs={'placeholder':'Enter full name'}),
              'email':forms.EmailInput(attrs={'placeholder':'Enter email'}),
              'phone':forms.TextInput(attrs={'placeholder':'Enter phon number'}),
              'deartment':forms.TextInput(attrs={'placeholder':'Enter department'})
         }


class UserRegistrationForm(UserCreationForm):
     email=forms.EmailField(required=True)
     class Meta:
          model=User
          fields=['username','email','password1','password2']

class UserLoginForm(AuthenticationForm):
     class Meta:
          model=User
          fields=['username',  'password']