from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .forms import NewPostForm 
from post.models import Post
from product.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

# Create your views here.


@login_required
def home_view(request):
    posts_feed = []
    userProfile = Profile.objects.get(user=request.user)
    posts_per_page = 10
    error = ""
    page = 2
    #try:
    products = random.sample(list(Product.objects.all()),5)
    users_following = userProfile.following.all()
    for user in users_following:
        for post in Post.objects.filter(author=user):
            posts_feed.append(post)
    paginator = Paginator(posts_feed, posts_per_page)
    #except:
     #   error = "Ninguém postou nada ultimamente! Experimente seguir mais pessoas, produtos e marcas!"

    if request.method == "POST":
        paginator = Paginator(
            posts_feed, posts_per_page + int(request.POST.get("page"))
        )
        page = int(request.POST.get("page")) + posts_per_page
    
    
    return render(
        request,
        "post/post-list.html",
        {
            "user": userProfile,
            "users": users_following,
            "posts_feed": paginator.page(1),
            "page": page,
            "error": error,
            "num_pages": paginator.num_pages,
            "products": products
        },
    )


@login_required
def craete_post_view(request):
    
    redirect("post:home")

@login_required
def explorer_view(request,page):
    userProfile = Profile.objects.get(user=request.user)
    posts_per_page = 5
    error = ""
    page = 1
    try:
        products = random.sample(list(Product.objects.all()),5)
        posts_feed = Post.objects.all()
        users_following = userProfile.following.all()
        paginator = Paginator(posts_feed, posts_per_page)
    except:
        error = "Ninguém postou nada ultimamente! Experimente seguir mais pessoas, produtos e marcas!"

    return render(
        request,
        "post/explorer-list.html",
        {
            "user": userProfile,
            "users": users_following,
            "posts_feed": paginator.page(page),
            "error": error,
            "num_pages": paginator.num_pages,
            "products" : products
        },
    )
