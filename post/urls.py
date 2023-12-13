from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("<str:page>/"),
    path("explorar/", views.explorer_view, name="explorer"),
    path("explorar/<str:page>/", views.explorer_view, name="explorer"),
]
