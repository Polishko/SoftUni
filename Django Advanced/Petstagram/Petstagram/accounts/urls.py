from django.contrib.auth.views import LogoutView
from django.urls import path, include
from Petstagram.accounts import views


urlpatterns = [
    path('register', views.AppUserRegisterView.as_view(), name='register'),
    path('login', views.AppUserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('profile/<int:pk>/', include([ not secure
    path('profile/', include([
        path('', views.ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='edit_profile'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete_profile'),
    ])),
]