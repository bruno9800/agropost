from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile,User

# Create your views here.


def login_view(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")
        try:
            username = User.objects.get(email=email.lower())
            user = authenticate(request, username=username, password=password,)
            if user is not None:
                login(request, user)
                return redirect("users:logged")
        except:
            return render(request, "users/login.html", {"erro": "Este usuário não existe"})

@login_required
def logged_view(request):
    count = 1
    userProfile = Profile.objects.get(user=request.user)
    if request.method == 'GET':
        feed_count = count
        users_following = userProfile.following.all()[:feed_count]
    if request.method == 'POST':
        users_current = request.POST.get('users')
        print(users_current)
        users_following = userProfile.following.all()[:count+int(users_current)]
        

        print(users_following)
    return render(request, "home/index.html", {"user": userProfile,"users":users_following})


@login_required
def logout_view(request):
    logout(request)
    return redirect("users:login")
