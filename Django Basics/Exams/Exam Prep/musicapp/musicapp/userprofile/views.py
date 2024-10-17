from django.shortcuts import render


def profile_details(request):
    context = {}
    return render(request, 'userprofile/profile-details.html', context)


def profile_delete(request):
    context = {}
    return render(request, 'userprofile/profile-delete.html', context)
