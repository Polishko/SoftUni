from django.http import HttpResponse, Http404
from django.shortcuts import render

from urlsAndViews.departments.models import Department


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world!</h1>')


# catch with *kwargs
# def view_with_name(request, *args, **kwargs):
#     return HttpResponse(f'<h1>Kwargs: {kwargs}</h1>')

# catch with url variable name
def view_with_name(request, param):
    return HttpResponse(f'<h1>Variable: {param}</h1>')


def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>Int pk with pk: {pk}</h1>')


def view_with_slug(request, pk, slug):
    try:
        department = Department.objects.get(pk=pk, slug=slug)
        return HttpResponse(f'<h1>Department with slug: {department}</h1>')
    except Department.DoesNotExist:
        raise Http404('No such department!')
