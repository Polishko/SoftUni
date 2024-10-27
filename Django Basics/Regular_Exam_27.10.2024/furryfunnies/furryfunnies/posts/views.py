from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from furryfunnies.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from furryfunnies.posts.models import Post
from furryfunnies.utils import get_user_object


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = get_user_object()
        post.save()

        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'post_id'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostDeleteForm(instance=self.object)

        return context
