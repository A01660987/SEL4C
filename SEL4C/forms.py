from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = self.instance
        if user.is_staff:   
            user.is_superuser = True
        return super().save(commit=True)
    class Meta:
        model = User
        fields = ('username', 'name', 'first_lastname', 'second_lastname')


class UserChangeForm(UserChangeForm):
    def save(self, commit=True):
        user = self.instance
        if user.is_staff:   
            user.is_superuser = True
        return super().save(commit=True)
    class Meta:
        model = User
        fields = ('username', 'name', 'first_lastname', 'second_lastname')