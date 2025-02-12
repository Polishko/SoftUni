from django.forms import modelform_factory
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet, PostBaseForm
from forumApp.posts.models import Post, Comment

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
        form = PostBaseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = PostBaseForm()


    context = {
        'my_form': form,
    }

    return render(request, 'posts/../../templates/common/index.html', context)

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
    form = PostCreateForm (request.POST or None, request.FILES or None)

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

    # Pass the queryset to allow for editing of associated comments
    comment_formset = CommentFormSet(request.POST or None, queryset=Comment.objects.filter(post=post))

    if request.method == 'POST':
        if comment_formset.is_valid():
            for comment_form in comment_formset:
                if comment_form.cleaned_data.get('author') and comment_form.cleaned_data.get('content'):
                    comment = comment_form.save(commit=False)
                    comment.post = post
                    comment.save()
        else:
            print(comment_formset.errors)


        return redirect('details-post', pk=post.id)

    context = {
        'post': post,
        'comment_formset': comment_formset
    }

    return render(request, 'posts/details-post.html', context)
