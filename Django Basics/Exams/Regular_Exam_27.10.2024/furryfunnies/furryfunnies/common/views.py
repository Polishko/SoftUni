from django.shortcuts import render
from django.views.generic import ListView

from furryfunnies.posts.models import Post


def show_index(request):
    return render(request, 'common/index.html')

class PostListView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'

