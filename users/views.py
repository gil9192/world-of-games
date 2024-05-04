from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import User


# Create your views here.


def get_user(username) -> User:
    try:
        return User.objects.get(username=username)
    except Exception as error:
        print(f"Encountered and error: {error}")
    return None


def login(request) -> HttpResponse:
    context = dict()
    context["authorized"] = request.session.get("authorized")
    context["username"] = request.session.get("username")
    if request.POST:
        user = get_user(request.POST["username"])
        if user and user.password == request.POST["password"]:
            request.session["authorized"] = True
            request.session["username"] = request.POST["username"]
            return HttpResponseRedirect(reverse("menu"))
        else:
            request.session["authorized"] = False
            context["msg"] = "Invalid Credentials!"
            print(request.session["authorized"])
            return render(request, "users/login.html", context)
    else:
        return render(request, "users/login.html", context)


def logout(request)  -> HttpResponse:
    context = dict()
    request.session["authorized"] = False
    context["authorized"] = request.session.get("authorized")
    context["username"] = request.session.get("username")
    print("Logout successful...")
    print(request.session["authorized"])
    return HttpResponseRedirect(reverse("menu"))


def register(request) -> HttpResponse:
    context = dict()
    context["authorized"] = request.session.get("authorized")
    context["username"] = request.session.get("username")
    if context["authorized"]:
        return HttpResponseRedirect(reverse("menu"))
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        verification_password = request.POST["verification_password"]
        print(username, password, verification_password)
        if password != verification_password:
            context["msg"] = "Passwords Don't Match."
            return render(request, "users/register.html", context)
        if get_user(username):
            context["msg"] = "User Already Exists..."
            return render(request, "users/register.html", context)
        new_user = User(username=username, password=password, score = 0)
        new_user.save()
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "users/register.html", context)
