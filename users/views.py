from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile, User, AnonymousUser
from post.models import Post
import datetime

# Create your views here.

def profile_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "profile/index.html")

def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            print(request.user)
            return redirect("users:logged")
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
                return redirect("users:logged")
        except:
            return render(request, "users/login.html", {"erro": "Este usuário não existe"})


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
        print(birth)
        now = datetime.datetime.now()
        birthdate = datetime.datetime.strptime(birth, "%Y-%m-%d")
        age = (now - birthdate) // 365
        if userAlreadyExists.exists():
            print(userAlreadyExists)
            return render(request, "users/signup.html", {"erro": "Este usuário já existe"})
        if password != password_confirm:
            return render(request, "users/signup.html", {"erro": "As senhas inseridas são diferentes!"})
        if age.days < 14:
            return render(request, "users/signup.html", {"erro": "Idade inválida! Você precisa ter mais de 14 anos!"})

        user = User.objects.create_user(username=email, email=email, password=password,)
        user.first_name, user.last_name = firstname, lastname
        user.save()

        Profile.objects.create(user=user, date_of_birth=birthdate)

        return redirect("users:login")


@login_required
def logged_view(request):
    posts_feed = []
    userProfile = Profile.objects.get(user=request.user)

    if request.method == "GET":
        #try:
            users_following = userProfile.following.all()
            for user in users_following:
                for post in Post.objects.filter(author=user):
                    posts_feed.append(post)
                    
            print(posts_feed)
               
        #except:
           #  return render(request, "home/index.html", {"error":"Ninguém postou nada ultimamente! Experimente seguir mais pessoas!"})
    if request.method == "POST":
       # try:
            users_current = request.POST.get("users")
            print(users_current)
            users_following = userProfile.following.all()[:int(users_current)+count_post]
            for user in users_following:
                 posts_feed = posts_feed.union(Post.objects.filter(author=user)[:count_post])
       # except:
            #return render(request, "home/index.html", {"error":"Por enquanto, isso é tudo! Exmperimente seguir mais pessoas"})

    return render(request, "home/index.html", {"user": userProfile,"users":users_following,"posts_feed":posts_feed})

@login_required
def logout_view(request):
    logout(request)
    return redirect("users:login")
