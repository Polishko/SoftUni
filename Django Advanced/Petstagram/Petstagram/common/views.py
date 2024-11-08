from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, resolve_url, get_object_or_404
from django.template.context_processors import request
from django.views.generic import ListView, CreateView
from pyperclip import copy

from Petstagram.common.forms import CommentForm, SearchForm
from Petstagram.common.models import Like, Comment
from Petstagram.photos.models import Photo

class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos' # by default object_list and photos
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        pet_name = self.request.GET.get('pet_name')
        if pet_name:
            queryset = queryset.filter(
                tagged_pets__name__icontains=pet_name
            )

        return queryset

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)

       context['comment_form'] = CommentForm()
       context['search_form'] = SearchForm(self.request.GET)

       user = self.request.user

       for photo in context['all_photos']:
           photo.has_liked = photo.likes.filter(user=user).exists() if user.is_authenticated else False

       return context

@login_required
def like_functionality(request, photo_id: int):
    photo = get_object_or_404(Photo, pk=photo_id)
    liked_object = Like.objects.filter(
        to_photo_id=photo_id,
        user=request.user
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo_id=photo.id, user=request.user)
        like.save()

    return redirect((request.META.get('HTTP_REFERER', '/')) + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))

    return redirect((request.META.get('HTTP_REFERER', '/')) + f'#{photo_id}')


class CreateCommentView(LoginRequiredMixin, CreateView):
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
        comment.user = self.request.user
        comment.save()

        return redirect(f"{self.request.META.get('HTTP_REFERER', '/')}#{self.photo.pk}")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
