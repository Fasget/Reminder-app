from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from myproject import urls
from .forms import UserRegistrationForm, UserLoginForm


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('category_list')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            user = form.save(commit=False)
            # Set the chosen password
            user.set_password(form.cleaned_data['password'])
            # Save the User object
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def base_view(request):
    return render(request, 'myapp/reminder_list.html')