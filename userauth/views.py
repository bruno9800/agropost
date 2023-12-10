from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

# Create your views here.


class CustomPasswordResetView(PasswordResetView):
    template_name = "userauth/reset-password.html"


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "userauth/reset-password-done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "userauth/reset-password-confirm.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "userauth/reset-password-complete.html"
