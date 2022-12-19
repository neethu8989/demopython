from django.forms import models

from .models import Task
from django import forms


class TodoForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
