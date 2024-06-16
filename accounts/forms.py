from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2", "avatar")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = f"{user.first_name}-{user.last_name}".lower()  # Set the username
        if commit:
            user.save()
            if self.cleaned_data["avatar"]:
                profile = user.userprofile
                profile.avatar = self.cleaned_data["avatar"]
                profile.save()
        return user
