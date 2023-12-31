import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from .models import Profile, User, AnonymousUser
from post.models import Post

import datetime

# Create your views here.


def profile_view(request, username):

    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user)
        followers = Profile.objects.filter(following=user.id)
        following = user.profile.following.all()
    except User.DoesNotExist:
        return render(request, "post/home.html")
    if request.method == "POST":
        print(request.POST['profile_id'])
        profile_to_follow = Profile.objects.get(id=request.POST['profile_id'])
        if profile_to_follow.user in request.user.profile.following.all():
            request.user.profile.following.remove(profile_to_follow.user)
        else:
            request.user.profile.following.add(profile_to_follow.user)
    print(followers)
    return render(request, "post/profile.html", {"profile_user": user,"posts":posts, "followers":followers, "following": following})

        

def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("post:home")
        return render(request, "users/login.html")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")

        try:
            username = User.objects.get(email=email.lower())
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("post:home")
            else:
                return render(request, "users/login.html", {"erro": "Senha incorreta"})

        except:
            return render(
                request, "users/login.html", {"erro": "Este usuário não existe"}
            )


def signup_view(request):
    if request.method == "GET":
        return render(request, "users/signup.html")
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        password_confirm = request.POST.get("pass2")
        birth = request.POST.get("birth")
        userAlreadyExists = User.objects.filter(email=email)
        now = datetime.datetime.now()
        birthdate = datetime.datetime.strptime(birth, "%Y-%m-%d")
        age = (now - birthdate) // 365
        if userAlreadyExists.exists():
            print(userAlreadyExists)
            return render(
                request, "users/signup.html", {"erro": "Este usuário já existe"}
            )
        if password != password_confirm:
            return render(
                request,
                "users/signup.html",
                {"erro": "As senhas inseridas são diferentes!"},
            )
        if age.days < 14:
            return render(
                request,
                "users/signup.html",
                {"erro": "Idade inválida! Você precisa ter mais de 14 anos!"},
            )

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
        )
        user.first_name, user.last_name = firstname, lastname
        user.save()

        Profile.objects.create(user=user, date_of_birth=birthdate)

        return redirect("users:login")


@login_required
def logout_view(request):
    logout(request)
    return redirect("users:login")


# class Views
