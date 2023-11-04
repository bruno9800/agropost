from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
  if request.method == 'GET':
    return render(request, 'users/login.html')
  if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('pass')
      