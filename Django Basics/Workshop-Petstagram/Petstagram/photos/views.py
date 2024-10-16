from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Petstagram.common.forms import CommentForm
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstagram.photos.models import Photo

class PhotoCreateView(CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.get_object()
        context['comments'] = photo.comments.all()
        context['likes'] = photo.likes.all()
        context['comment_form'] = CommentForm()

        return context


class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    context_object_name = 'photo'
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        # Instead of rendering a confirmation or GET page, proceed to deletion
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        photo = self.get_object()
        photo.tagged_pets.clear()
        return super().delete(request, *args, **kwargs)
    