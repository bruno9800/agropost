from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("explorar/", views.explorer_view, name="explorer"),
]
