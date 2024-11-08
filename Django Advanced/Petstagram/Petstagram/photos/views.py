from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Petstagram.common.forms import CommentForm
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstagram.photos.models import Photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        # photo.save()
        # form.save_m2m() # m-to-m fields are saved separately

        return super().form_valid(form) # this executes the saves above


class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'
    # context_object_name = 'photo' # the view provides this

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.object
        context['comments'] = photo.comments.all()
        context['likes'] = photo.likes.all()
        context['comment_form'] = CommentForm()
        self.object.has_liked = self.object.likes.filter(user=self.request.user).exists() #alternative to adding as context

        return context


class PhotoEditView(LoginRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoEditForm
    context_object_name = 'photo'
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})

@login_required
@require_POST  # Only allow POST requests to trigger deletion
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if photo.user == request.user:  # Optional: Check ownership if needed
        photo.delete()
    return redirect(reverse('home'))

# not safe
# class PhotoDeleteView(LoginRequiredMixin, DeleteView):
#     model = Photo
#     success_url = reverse_lazy('home')
#
#     def get(self, request, *args, **kwargs):
#         # Instead of rendering a confirmation or GET page, proceed to deletion
#         return self.delete(request, *args, **kwargs)
