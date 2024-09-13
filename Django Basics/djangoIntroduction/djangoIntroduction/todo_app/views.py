from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    result = '\n'.join([
        '<h1>TASKS</h1>',
        '<ul>',
        *[f"<li>{task.name}</li>" for task in tasks],
        '</ul>'
    ])
    return HttpResponse(result)

