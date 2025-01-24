from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

from .models import Reminder, Category
from .forms import ReminderForm, CategoryForm, UserForm, ChangePasswordForm

@login_required
def personal_account(request):
    user_form = UserForm(request.POST, instance=request.user)
    password_form = ChangePasswordForm(user=request.user, data=request.POST)
    if password_form.has_changed() and password_form.is_valid():
        password_form.save()
        update_session_auth_hash(request, password_form.user)
        messages.success(request, 'Пароль успешно изменен.', extra_tags='change-password')
        return redirect('personal_account')
    else:
        redirect('personal_account')
    if request.method == 'POST':


        # Проверяем, были ли отправлены данные для изменения профиля пользователя
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Профиль успешно обновлен.', extra_tags='update-profile')
            return redirect('personal_account')

    else:
        user_form = UserForm(instance=request.user)
        password_form = ChangePasswordForm(user=request.user)

    context = {
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'myapp/personal_account.html', context)

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'myapp/category_list.html', {'categories': categories})

@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user  # set the user field to the current user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'myapp/category_new.html', {'form': form})


@login_required
def reminder_list(request, category):
    category = get_object_or_404(Category, pk=category)
    reminders = Reminder.objects.filter(category=category)
    return render(request, 'myapp/reminder_list.html', {'category': category, 'reminders': reminders})


def reminder_detail(request, pk, category):
    category = get_object_or_404(Category, pk=category)
    reminder = get_object_or_404(Reminder, pk=pk)
    return render(request, 'myapp/reminder_detail.html', {'category': category, 'reminder': reminder})


@login_required
@login_required
def reminder_new(request, category):
    category = get_object_or_404(Category, pk=category)
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.category = category
            reminder.save()
            return redirect(reverse('reminder_detail', kwargs={'category': category.pk, 'pk': reminder.pk}))
    else:
        form = ReminderForm()

    # Redirect to category list view if category is not provided
    if not category:
        return redirect('category_list')

    return render(request, 'myapp/reminder_edit.html', {'form': form})

@login_required
def category_edit(request, category):
    category = get_object_or_404(Category, pk=category, user=request.user)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'myapp/category_edit.html', {'form': form})


def reminder_edit(request, pk, category):
    category = get_object_or_404(Category, pk=category)
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == "POST":
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.save()
            return redirect('reminder_detail', pk=reminder.pk, category=category.id)
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'myapp/reminder_edit.html', {'form': form})


def category_delete(request, category):
    category = get_object_or_404(Category, pk=category)
    reminders = Reminder.objects.filter(category=category)
    reminders.delete()
    category.delete()
    return redirect(reverse('category_list'))

def reminder_delete(request, pk, category):
    category = get_object_or_404(Category, pk=category)
    reminder = get_object_or_404(Reminder, pk=pk)
    reminders = Reminder.objects.filter(category=category)
    reminder.delete()
    return render(request, 'myapp/reminder_list.html', {'category': category, 'reminders': reminders})


@login_required
def uncompleted_all_reminders(request):
    reminders = Reminder.objects.filter()
    for reminder in reminders:
        reminder.completed=False
        reminder.save()
    return redirect('category_list')


@login_required
def completed_all_reminders(request):
    reminders = Reminder.objects.filter()
    for reminder in reminders:
        reminder.completed=True
        reminder.save()
    return redirect('category_list')

@login_required
def reminder_delete_all(request):
    Reminder.objects.filter(user=request.user).order_by('-date').all().delete()
    return redirect('category_list')


@login_required
def category_delete_all(request):
    categories = Category.objects.filter(user=request.user)
    for category in categories:
        reminders = Reminder.objects.filter(category=category)
        reminders.delete()
    categories.delete()
    return redirect('category_list')