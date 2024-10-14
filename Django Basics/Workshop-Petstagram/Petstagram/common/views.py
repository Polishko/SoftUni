from django.contrib.admin.templatetags.admin_list import search_form
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.views.generic import ListView
from pyperclip import copy

from Petstagram.common.forms import CommentForm, SearchForm
from Petstagram.common.models import Like
from Petstagram.photos.models import Photo


class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'

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

       photos_per_page = 1
       paginator = Paginator(context['all_photos'], photos_per_page)
       page = self.request.GET.get('page')

       try:
           context['all_photos'] = paginator.page(page)
       except PageNotAnInteger:
           context['all_photos'] = paginator.page(1)
       except EmptyPage:
           context['all_photos'] = paginator.page(paginator.num_pages)

       return context

def like_functionality(request, photo_id: int):
    # photo = Photo.objects.get(id=photo_id)
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

def comment_functionality(request, photo_id):
    if request.method == 'POST':
        photo = get_object_or_404(Photo, pk=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

    return redirect(f"{request.META.get('HTTP_REFERER', '/')}#{photo_id}")
