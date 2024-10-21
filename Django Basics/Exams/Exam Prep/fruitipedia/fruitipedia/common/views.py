from django.shortcuts import render

def show_index(request):
    return render(request, 'common/index.html')

def show_dashboard(request):
    return render(request, 'common/dashboard.html')