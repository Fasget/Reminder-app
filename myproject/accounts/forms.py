from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    error_messages = {
        'invalid_login': 'Неправильный логин или пароль',
    }

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не равны')
        return cd['password2']


