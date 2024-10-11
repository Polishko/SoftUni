from django.urls import path, include

from forumApp.posts.views import dashboard, add_post, delete_post, details_page, edit_post, Index, IndexView, \
    RedirectHomeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-post/', add_post, name='add-post'),
    path('<int:pk>/', include([
        path('details-post', details_page, name='details-post'),
        path('delete-post/', delete_post, name='delete-post'),
        path('edit-post/', edit_post, name='edit-post'),
    ])),
    path('redirect-home/', RedirectHomeView.as_view(), name='redirect-home')
]