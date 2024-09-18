import json
import pdb

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404

from viewsAndUrls.departments.models import Department


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world!</h1>')


# catch with *kwargs
# def view_with_name(request, *args, **kwargs):
#     return HttpResponse(f'<h1>Kwargs: {kwargs}</h1>')

# catch with url variable name
def view_with_name(request, variable):
    # return HttpResponse(f'<h1>Variable: {variable}</h1>')
    return render(request, 'departments/name_template.html', {'variable': variable})


def view_with_int_pk(request, pk):
    # return HttpResponse(f'<h1>Int pk with pk: {pk}</h1>')
    # return HttpResponse(f'<h1>Int pk with pk: {pk}</h1>', content_type='text/plain')
    # return HttpResponse(json.dumps({'pk': pk}), content_type='application/json')
    return JsonResponse({'pk': pk})


def view_with_slug(request, pk, slug):
    # try:
    #     department = Department.objects.get(pk=pk, slug=slug)
    #     return HttpResponse(f'<h1>Department with slug: {department}</h1>')
    # except Department.DoesNotExist:
    #     raise Http404('No such department!')

    # or filter and if not object raise error

    # or use the Django provided method that gets the model and the filter conditions
    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f'<h1>Department with slug: {department}</h1>')


def show_archive(request, archive_year):
    return HttpResponse(f'<h1>The year is: {archive_year}</h1>')


def simple_view(request):
    # pdb.set_trace()
    return HttpResponse("Hello, world!")