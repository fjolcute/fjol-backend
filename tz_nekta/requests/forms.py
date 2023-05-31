from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class AddRequestForm(forms.ModelForm):
   class Meta:
       model = Request
       fields = ('request',)

class AddMessageForm(forms.ModelForm):
   class Meta:
       model = RequestMessage
       fields = ('reqmail',)

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class FindRequestsInfo(forms.Form):
     requestid = forms.CharField(label='id заявки', max_length=255)




class AddMessageFormById(forms.ModelForm):
   class Meta:
       model = RequestMessage
       fields = ('reqmail', 'request')