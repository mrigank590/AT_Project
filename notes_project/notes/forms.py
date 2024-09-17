from django import forms
from django.contrib.auth.models import User
from .models import Note


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
