from datetime import datetime

from django.shortcuts import render, redirect

from forumApp.posts.forms import PostBaseForm
from forumApp.posts.models import Post


# Create your views here.
def  index(request):

    context = {
        'my_form': '',
    }

    return render(request, 'base.html', context)

def dashboard(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'posts/dashboard.html', context)

def add_post(request):
    form = PostBaseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'posts/add_form.html', context)