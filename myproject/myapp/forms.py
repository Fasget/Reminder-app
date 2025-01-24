from django import forms
from .models import Reminder, Category
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Повторите пароль',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Не правильный старый пароль")
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

class UserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'username': 'login',
            'email': 'email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'disc')
        labels = {
            'name': 'Название',
            'disc': 'Описание',
        }


class ReminderForm(forms.ModelForm):
    date = forms.DateTimeField(
        label='Дата и время',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    class Meta:
        model = Reminder
        fields = ('text', 'date', 'completed', 'description',)
        labels = {
            'text': 'Текст',
            'description': 'Описание',
            'completed': 'Выполнено',
        }
        widgets = {
            'date': forms.TextInput()
        }
