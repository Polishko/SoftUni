from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from musicapp.album.forms import AddAlbumForm, EditAlbumForm, DeleteAlbumForm
from musicapp.album.models import Album

from musicapp.utils import get_user_object


class AddAlbum(CreateView):
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy('home-page')
    template_name = 'album/album-add.html'

    def form_valid(self, form):
        album = form.save(commit=False)
        album.owner = get_user_object()
        album.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class AlbumDetails(DetailView):
    model = Album
    template_name = 'album/album-details.html'
    pk_url_kwarg = 'id'

class AlbumEdit(UpdateView):
    model = Album
    form_class = EditAlbumForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home-page')
    template_name = 'album/album-edit.html'

class AlbumDelete(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/album-delete.html'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteAlbumForm(instance=self.object)

        return context
