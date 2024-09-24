from django.shortcuts import render
from django.templatetags.static import static

def my_view(request):
    print(static('css/styles.css'))  # This will print the resolved URL to the console
    return render(request, 'accounts/login-page.html')

def register(request):
    return render(request, template_name='accounts/register-page.html')

def login(request):
    return render(request, template_name='accounts/login-page.html')

def show_profile_details(request):
    return render(request, template_name='accounts/profile-details-page.html')

def edit_profile(request):
    return render(request, template_name='accounts/profile-edit-page.html')

def delete_profile(request):
    return render(request, template_name='accounts/profile-delete-page.html')
