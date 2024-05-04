from django.shortcuts import render


# Create your views here.

def menu(request):
    context = dict()
    context["authorized"] = request.session.get("authorized")
    context["username"] = request.session.get("username")
    return render(request, "menu/menu.html", context)