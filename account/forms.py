from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class UserReg istrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':' please Enter strong password'}))
    password2 = forms.CharField(label='confrim password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':' please Enter strong password'}))


    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exists')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username already exists')
        return username