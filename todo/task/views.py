from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Tasks.objects.all()

    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'tasks': tasks, 'form':form}
    return render(request,'task/list.html', context)
