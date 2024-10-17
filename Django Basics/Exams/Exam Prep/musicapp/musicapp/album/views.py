from django.shortcuts import render

def album_add(request):
    context = {}
    return render(request, 'album/album-add.html', context)

def album_details(request, pk=int):
    context = {}
    return render(request, 'album/album-details.html', context)

def album_edit(request, pk=int):
    context = {}
    return render(request, 'album/album-edit.html', context)

def album_delete(request, pk=int):
    context = {}
    return render(request, 'album/album-delete.html', context)
