import imp
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class WishlistForm(forms.Form):

    username = forms.CharField(max_length=50)
    isbn = forms.CharField(max_length=13)

class chatForm(forms.Form):  
    username = forms.CharField(label='', max_length=100)
    
class messageForm(forms.Form):  
    message = forms.CharField(label='', max_length=1000)

class ReportFraudForm(forms.Form):

    username = forms.CharField(max_length=50)
    report = forms.CharField(widget=forms.Textarea())




