from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furryfunnies.userprofile.forms import AuthorCreateForm, AuthorEditForm
from furryfunnies.userprofile.models import Author
from furryfunnies.utils import get_user_object


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'userprofile/create-author.html'
    success_url = reverse_lazy('dashboard')
    form_class = AuthorCreateForm


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'userprofile/details-author.html'

    def get_object(self, queryset=None):
        return get_user_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_post = self.object.post_set.order_by('-updated_at').first()
        context['latest_post'] = latest_post

        return context


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthEditForm
    template_name = 'userprofile/edit-author.html'
    success_url = reverse_lazy('author-detail')

    def get_object(self, queryset=None):
        return get_user_object()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'userprofile/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_object()
