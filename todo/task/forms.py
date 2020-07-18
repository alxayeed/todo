from django import forms
from django.forms import ModelForm

from .models import *

class TasksForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Something new to Your Bucket List!'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add a line of description to your goal!'}))

    class Meta:
        model = Tasks
        fields = '__all__'