from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile, User
from post.models import Post
from product.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


@login_required
def home_view(request):
    posts_feed = []
    userProfile = Profile.objects.get(user=request.user)
    posts_per_page = 1
    error = ""
    page = 2
    try:
        products = Product.objects.all()
        users_following = userProfile.following.all()[:5]
        for user in users_following:
            for post in Post.objects.filter(author=user):
                posts_feed.append(post)
        paginator = Paginator(posts_feed, posts_per_page)
    except:
        error = "Ninguém postou nada ultimamente! Experimente seguir mais pessoas, produtos e marcas!"

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
            "products": products,
        },
    )


@login_required
def explorer_view(request):
    userProfile = Profile.objects.get(user=request.user)
    posts_per_page = 1
    error = ""
    page = 2
    try:
        posts_feed = Post.objects.all()
        users_following = userProfile.following.all()
        paginator = Paginator(posts_feed, posts_per_page)
    except:
        error = "Ninguém postou nada ultimamente! Experimente seguir mais pessoas, produtos e marcas!"

    if request.method == "POST":
        paginator = Paginator(
            posts_feed, posts_per_page + int(request.POST.get("page"))
        )
        page = int(request.POST.get("page")) + posts_per_page

    return render(
        request,
        "post/explorer-list.html",
        {
            "user": userProfile,
            "users": users_following,
            "posts_feed": paginator.page(1),
            "page": page,
            "error": error,
            "num_pages": paginator.num_pages,
        },
    )
