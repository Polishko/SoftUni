from django.urls import path, include
from Petstagram.accounts import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='edit_profile'),
        path('delete/', views.profile_delete, name='delete_profile'),
    ])),
]