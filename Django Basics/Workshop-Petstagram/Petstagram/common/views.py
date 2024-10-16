from django.shortcuts import redirect, resolve_url, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from pyperclip import copy

from Petstagram.common.forms import CommentForm, SearchForm
from Petstagram.common.models import Like, Comment
from Petstagram.photos.models import Photo

class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_queryset(self):
        all_photos = Photo.objects.all()

        search_form = SearchForm(self.request.GET)
        if search_form.is_valid():
            all_photos = all_photos.filter(
                tagged_pets__name__icontains=search_form.cleaned_data['pet_name']
            )

        return all_photos

    def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(**kwargs)

       context['comment_form'] = CommentForm()
       context['search_form'] = SearchForm(self.request.GET)

       return context

def like_functionality(request, photo_id: int):
    photo = get_object_or_404(Photo, pk=photo_id)
    liked_object = Like.objects.filter(
        to_photo_id=photo_id
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo_id=photo.id)
        like.save()

    return redirect((request.META.get('HTTP_REFERER', '/')) + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))

    return redirect((request.META.get('HTTP_REFERER', '/')) + f'#{photo_id}')


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._photo = None

    # fetch photo lazily from DB only once and store as attr for cache
    @property
    def photo(self):
        if self._photo is None:
            self._photo = get_object_or_404(Photo, pk=self.kwargs['photo_id'])
        return self._photo

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.to_photo = self.photo
        comment.save()

        return redirect(f"{self.request.META.get('HTTP_REFERER', '/')}#{self.photo.pk}")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
