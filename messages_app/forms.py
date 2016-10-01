from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


from models import NotificationUser


@csrf_exempt
class NotificationForm(forms.ModelForm):
    """
    @csrf_exempt disables the csrf protection.
    """
    class Meta:
        model = NotificationUser
        fields = ('title', 'message', 'user')
