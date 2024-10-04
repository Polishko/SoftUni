from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostBaseForm, PostCreateForm, PostDeleteForm, SearchForm, PostEditForm
from forumApp.posts.models import Post


PostForm = modelform_factory(
        Post,
        fields=('title', 'content', 'author'),
        error_messages={
            'title': {
                'required': 'Title is required',
            }
        }
    )
def  index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = PostForm()


    context = {
        'my_form': form,
    }

    return render(request, 'posts/common/index.html', context)

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

    return render(request, 'posts/add_post.html', context)

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
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        '''
        instance=post: This tells Django that the form is bound to the existing post instance.
        By providing the instance argument,
        Django knows this form should update the existing post rather than creating a new one.
        '''
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = PostEditForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'posts/edit-post.html', context)

def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post
    }

    return render(request, 'posts/details-post.html', context)
