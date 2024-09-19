
from django.urls import path, re_path, include
from viewsAndUrls.departments import views


urlpatterns = [
    path('', views.index, name='home'),
    path('reverse/', views.reverse_view),
    path('softuni/', views.redirect_to_softuni),
    path('redirect-to-view/', views.redirect_to_view, name='redirect-view'),
    path('simple/', views.simple_view),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk, name='num_pk'),
        path('<int:pk>/<slug:slug>', views.view_with_slug),

    ])),
    path('<variable>/', views.view_with_name),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
    # path('<path:variable>/', views.view_with_name),
    # path('<uuid:id>/'),
]
