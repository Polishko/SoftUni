from django.urls import path

from Petstagram.common import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('like/<int:photo_id>', views.like_functionality, name='like'),
    path('share/<int:photo_id>', views.copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>', views.CreateCommentView.as_view(), name='comment'),
]
