from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world!</h1>')


# catch with *kwargs
def view_with_name(request, *args, **kwargs):
    return HttpResponse(f'<h1>Kwargs: {kwargs}</h1>')

# catch with url variable name
# def view_with_name(request, param):
#     return HttpResponse(f'<h1>Kwargs: {param}</h1>')
