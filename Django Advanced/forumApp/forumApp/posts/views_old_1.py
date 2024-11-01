from datetime import datetime
from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render

from forumApp.posts.forms import PersonForm


# Create your views here.
def  index(request):
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['person_name'])

    context = {
        'my_form': form,
    }

    return render(request, 'posts/common/base.html', context)

def dashboard(request):
    context = {
        'posts':[
            {
                'title': 'How to create a Django project 1?',
                'author': 'Nalan',
                'content': 'I know **a little** about <i>creating</i> a Django project.',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create a Django project 2?',
                'author': '',
                'content': '###I know a little about creating a Django project.',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create a Django project 3?',
                'author': 'Nalan',
                'content': '',
                'created_at': datetime.now(),
            },

        ]
    }

    return render(request, 'posts/dashboard.html', context)
