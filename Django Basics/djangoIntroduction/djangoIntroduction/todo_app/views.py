from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    print(tasks)

    result = '\n'.join([
        '<ul>',
        *[f'<li>{task}<li>' for task in tasks],
        '</ul>'
    ])
    return HttpResponse(result)

