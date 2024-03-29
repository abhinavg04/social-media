from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm

class ChangePassword(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1','new_password2']


class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))
    password = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))