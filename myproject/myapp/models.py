from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    disc = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def is_valid(self):
        pass


class Reminder(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

