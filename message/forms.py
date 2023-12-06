from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль1', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пороля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    avatar = forms.ImageField(label='Аватар', widget=forms.ClearableFileInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'email', 'password2', 'avatar')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))