from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from users.models import User

# Create your views here.


def scores(request):
    context = dict()
    context["users"] = User.objects.all().order_by("-score")
    context["authorized"] = request.session.get("authorized")
    context["username"] = request.session.get("username")
    if context["authorized"] == True:
        return render(request, "scores/scores.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))
