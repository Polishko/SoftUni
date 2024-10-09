from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect

from Petstagram.common.forms import CommentForm
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstagram.photos.models import Photo


# Create your views here.
def photo_add_page(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)

def photo_details_page(request, pk: int):
    photo = get_object_or_404(Photo, pk=pk)
    comments = photo.comment_set.all()
    likes = photo.like_set.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes,
        'comment_form': comment_form,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)

def photo_edit_page(request, pk: int):
    photo = get_object_or_404(Photo, pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, template_name='photos/photo-edit-page.html', context=context)

def photo_delete_page(request, pk: int):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('home')
