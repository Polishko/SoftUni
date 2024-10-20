from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from musicapp.album.forms import AddAlbumForm, EditAlbumForm
from musicapp.album.models import Album
from musicapp.userprofile.models import Profile


class AddAlbum(CreateView):
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy('home-page')
    template_name = 'album/album-add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()

        return context

    def form_valid(self, form):
        album = form.save(commit=False)
        current_user_id = self.request.session.get('profile_id')
        current_user = get_object_or_404(Profile, pk=current_user_id)
        album.owner = current_user
        album.save()

        return redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

# FBV option
# def album_add(request):
#     form = AddAlbumForm(request.POST or None)
#
#
#     if request.method == 'POST':
#         if form.is_valid():
#             album = form.save(commit=False)
#             current_user_id = request.session.get('profile_id')
#             current_user = get_object_or_404(Profile, pk=current_user_id)
#             album.owner = current_user
#             album.save()
#
#             return redirect('home-page')
#
#     return render(request, 'album/album-add.html', {'form': form})

class AlbumDetails(DetailView):
    model = Album
    template_name = 'album/album-details.html'
    context_object_name = 'album' # optional

# FBV option
# def album_details(request, pk):
#     album = get_object_or_404(Album, pk=pk)
#
#     return render(request, 'album/album-details.html', {'album': album})

class AlbumEdit(UpdateView):
    model = Album
    form_class = EditAlbumForm
    success_url = reverse_lazy('home-page')
    template_name = 'album/album-edit.html'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

# FBV option
# def album_edit(request, pk):
#     album = get_object_or_404(Album, pk=pk)
#     form = EditAlbumForm(request.POST or None, instance=album)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('home-page')
#
#     return render(request, 'album/album-edit.html', {'form': form})

def album_delete(request, pk=int):
    context = {}
    return render(request, 'album/album-delete.html', context)
