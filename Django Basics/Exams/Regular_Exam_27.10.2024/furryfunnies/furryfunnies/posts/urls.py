from django.urls import path, include

from furryfunnies.posts.views import PostCreateView, PostEditView, PostDetailView, PostDeleteView


urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/', include([
        path('details/', PostDetailView.as_view(), name='post-detail'),
        path('edit/', PostEditView.as_view(), name='post-edit'),
        path('delete/', PostDeleteView.as_view(), name='post-delete'),
    ]))
]