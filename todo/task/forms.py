from django import forms
from django.forms import ModelForm

from .models import *

class TasksForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Something new to Your Bucket List!'}))

    class Meta:
        model = Tasks
        fields = '__all__'