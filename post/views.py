from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from users.models import Profile, User
from post.models import Post
import datetime
# Create your views here.


@login_required
def home_view(request):
    posts_feed = []
    userProfile = Profile.objects.get(user=request.user)

    if request.method == "GET":
        # try:
        users_following = userProfile.following.all()
        for user in users_following:
            for post in Post.objects.filter(author=user):
                posts_feed.append(post)

        print(posts_feed)

    # except:
    #  return render(request, "home/index.html", {"error":"Ninguém postou nada ultimamente! Experimente seguir mais pessoas!"})
    if request.method == "POST":
        # try:
        users_current = request.POST.get("users")
        print(users_current)
        users_following = userProfile.following.all()[: int(users_current) + count_post]
        for user in users_following:
            posts_feed = posts_feed.union(Post.objects.filter(author=user)[:count_post])
    # except:
    # return render(request, "home/index.html", {"error":"Por enquanto, isso é tudo! Exmperimente seguir mais pessoas"})

    return render(
        request,
        "post/home.html",
        {"user": userProfile, "users": users_following, "posts_feed": posts_feed},
    )
