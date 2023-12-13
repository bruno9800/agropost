from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.home_view_redirect, name="home"),
    path("create", views.create_post_view, name="create"),
    path("<int:page>/", views.home_view, name="home_pagination"),
    path("explorar/", views.explorer_view_redirect, name="explorer"),
    path("explorar/<int:page>/", views.explorer_view, name="explorer_pagination"),
    path('post/<int:id>', views.post_view, name='post_view'),
    path('post/comment',views.create_comment, name="create_comment"),
]

