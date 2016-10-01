from django import forms
from django.contrib.auth.models import User
from models import WeakUser


class UserCreationForm(forms.ModelForm):
    """
    Form to create a new user.
    is_superuser is included in the form but not displayed during the
    rendering making the app vulnerable to request tampering that might
    lead to privilege escalation .
    """
    class Meta:
        model = User
        fields = ("username", "password", "is_superuser")
