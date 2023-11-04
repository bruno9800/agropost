from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("sign-in", views.login_view, name="login"),
    path("", views.logged_view, name="logged"),
    path("logout/", views.logout_view, name="logout"),
]
