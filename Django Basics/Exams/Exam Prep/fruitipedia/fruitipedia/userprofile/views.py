from django.shortcuts import render

def profile_create(request):
    return render(request, 'userprofile/create-profile.html')

def profile_details(request):
    return render(request, 'userprofile/details-profile.html')

def profile_edit(request):
    return render(request, 'userprofile/edit-profile.html')

def profile_delete(request):
    return render(request, 'userprofile/delete-profile.html')
