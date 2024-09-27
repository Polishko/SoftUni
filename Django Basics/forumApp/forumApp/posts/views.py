from datetime import datetime

from django.shortcuts import render


# Create your views here.
def  index(request):

    context = {
        'my_form': '',
    }

    return render(request, 'base.html', context)

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
