from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput
    (attrs={'class':'form-control','placeholder':'your password'}))
