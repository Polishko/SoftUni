from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


# Create your views here.
def index(request):
    title_filter = request.GET.get("title_filter", "")
    tasks = Task.objects.filter(name__icontains=title_filter)

    # tasks = Task.objects.all()

    context = {
        'title_filter': title_filter,
        'tasks': tasks
    }

    return render(request, 'todo_app/index.html', context)


# def index(request):
#     todo_app = Task.objects.all()

    # result = '\n'.join([
    #     '<h1>TASKS</h1>',
    #     '<ul>',
    #     *[f"<li>{task.name}</li>" for task in todo_app],
    #     '</ul>'
    # ])
    # return HttpResponse(result)


