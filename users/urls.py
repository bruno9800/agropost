from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("sign-in", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("profile/<str:username>/", views.profile_view, name="profile"),
]
