# product/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
from post.models import Post

def profile_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    posts = Post.objects.filter(product=product)

    return render(
        request,
        "product/profile.html",
        {"product": product,
         "posts":posts         
        }
    )
