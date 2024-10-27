from django.urls import path

from furryfunnies.common.views import show_index, PostListView

urlpatterns = [
    path('', show_index, name='index'),
    path('dashboard/', PostListView.as_view(), name='dashboard'),
]
