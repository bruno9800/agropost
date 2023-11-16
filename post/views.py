from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from users.models import Profile, User
from post.models import Post
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


@login_required
def home_view(request):
    posts_feed = []
    userProfile = Profile.objects.get(user=request.user)
    posts_per_page = 2
    error = ""

    try:
        users_following = userProfile.following.all()
        for user in users_following:
            for post in Post.objects.filter(author=user):
                posts_feed.append(post)
        paginator = Paginator(posts_feed,posts_per_page)
    except:
        error = "Ninguém postou nada ultimamente! Experimente seguir mais pessoas, produtos e marcas!"

    if request.method == "GET":
        page = 1 

    if request.method == "POST":
        page = int(request.POST.get("page"))+1

    return render(
        request,
        "post/home.html",
        {"user": userProfile, "users": users_following, "posts_feed": paginator.page(page),"page":page,"error":error,"num_pages":paginator.num_pages},
    )
