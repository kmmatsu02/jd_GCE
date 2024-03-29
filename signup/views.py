from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreateFrom


def index(request):
    if request.method == "GET":
        context = {"form": UserCreateFrom}
        return render(request, "signup/home.html", context)
    form = UserCreateFrom(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "signup/home.html")
    else:
        return render(request, "signup/home.html", {"form": form})

def login_view(request):
    if request.method == "GET":
        return render(request, "signup/home.html")
    
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)
    login(request, user)
    return HttpResponseRedirect(reverse("blog:article"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("blog:article"))