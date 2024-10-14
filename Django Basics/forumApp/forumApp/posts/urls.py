from django.urls import path, include

from forumApp.posts.views import IndexView, \
    RedirectHomeView, DashboardView, AddPostView, EditPostView, DeletePostView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('details-post', PostDetailView.as_view(), name='details-post'),
        path('delete-post/', DeletePostView.as_view(), name='delete-post'),
        path('edit-post/', EditPostView.as_view(), name='edit-post'),
    ])),
    path('redirect-home/', RedirectHomeView.as_view(), name='redirect-home')
]