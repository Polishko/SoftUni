from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostBaseForm, PostCreateForm, PostDeleteForm, SearchForm
from forumApp.posts.models import Post


# Create your views here.
def  index(request):

    context = {
        'my_form': '',
    }

    return render(request, 'base.html', context)

def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data['query']
        posts = posts.filter(title__icontains=query)


    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'posts/dashboard.html', context)

def add_post(request):
    form = PostCreateForm (request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'posts/add_form.html', context)

def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(request.POST or None, instance=post)

    if request.method == 'POST' and form.is_valid():
        post.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'posts/delete-post.html', context)


def edit_post(request, pk: int):
    return HttpResponse(f'Here will come edit content for post {pk}')


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post
    }

    return render(request, 'posts/details-post.html', context)
