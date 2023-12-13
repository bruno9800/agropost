from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from post.models import Post, Comment
from product.models import Product,Brand
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

# Create your views here.



def home_view_redirect(request):
    return redirect('post:home_pagination', page=1)

@login_required
def home_view(request,page):
    posts_feed = []
    userProfile = Profile.objects.get(user=request.user)
    posts_per_page = 10
    error = ""
    #try:
    product_types = (
        ("vermifuga", "Vermifuga"),
        ("Adubo", "Adubo"),
        ("Veneno", "Veneno"),
        ("Fertilizante", "Fertilizante"),
        ("Agrotoxico", "Agrotoxico"),
        ("Fungicida","Fungicida"),
    )
    products = random.sample(list(Product.objects.all()),5)
    products_post = Product.objects.all()
    brands_post = Brand.objects.all()
    users_following = userProfile.following.all()
    for user in users_following:
        for post in Post.objects.filter(author=user):
            posts_feed.append(post)
    paginator = Paginator(posts_feed, posts_per_page)
    #except:
    #   error = "Ninguém postou nada ultimamente! Experimente seguir mais pessoas, produtos e marcas!"
    
    return render(
        request,
        "post/post-list.html",
        {
            "user": userProfile,
            "users": users_following,
            "posts_feed": paginator.page(page),
            "error": error,
            "num_pages": range(1,paginator.num_pages+1),
            "products": products,
            "products_post":products_post,
            "brands_post":brands_post,
            "product_types": product_types
        },
    )

def explorer_view_redirect(request):
    return redirect('post:explorer_pagination', page=1)

@login_required
def create_post_view(request):
    title = request.POST.get("post-title")
    content = request.POST.get("content")
    author = request.user
    product = Product.objects.get(name=request.POST.get("product-name"))
    
    Post.objects.create(title=title,content=content,author=author,product=product)
    return redirect("post:home")

@login_required
def explorer_view(request,page):
    userProfile = Profile.objects.get(user=request.user)
    posts_per_page = 10
    error = ""
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
            "num_pages": range(1,paginator.num_pages+1),
            "products" : products
        },
    )

@login_required
def post_view(request, id):
    post = Post.objects.get(id=id)
    coments = Comment.objects.filter(post=post)
    
    return render(request, "post/post-show.html", {'post': post,'comments': coments})

@login_required
def create_comment(request):
    content = request.POST.get("content")
    id_post = request.POST.get("id_post")
    post = Post.objects.get(id=int(id_post))
    Comment.objects.create(content=content,post=post,user=request.user)
    return redirect("post:post_view", id=id_post)
