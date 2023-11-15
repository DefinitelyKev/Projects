from django import forms
from django.forms import ModelForm
from .models import SubscribedUsers


class SubscribedUsersForm(ModelForm):
    class Meta:
        model = SubscribedUsers
        fields = "__all__"
