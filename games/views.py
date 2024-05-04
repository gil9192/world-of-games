import random
from currency_converter import CurrencyConverter

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from users.models import User

# Create your views here.


def get_user(username) -> User:
    try:
        return User.objects.get(username=username)
    except Exception as error:
        print(f"Encountered and error: {error}")
    return None


def isfloat(value: str) -> bool:
    """
    Check if input value is a string that
    representing a leagal floating point number.

    Args:
        value (str): Value to check.

    Returns:
        bool: True if leagal floating point number string, else False.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_money_interval(amount: int, difficulty: int) -> tuple:
    """
    Retrieves the current USD to ILS exchange rate and calculates an
    interval for the correct answer based on the game's difficulty level.

    Args:
        amount (int): Amount of USD that should be converted to ILS.
        difficulty (int): Game difficulty level.

    Returns:
        tuple: The minimal accaptable, and maximal accaptable values.
    """
    # Get currency via dedicated package.
    currency = CurrencyConverter().convert(1,"USD","ILS")
    delta = 10 - difficulty
    converted = amount * currency
    # No upper range limitations.
    max = converted + delta
    # Trim the lower range at 0.1, can't get negative values and 0 ILS.
    min = 0.1 if converted - delta < 0.1 else converted - delta
    return min, max


def games(request):
    context = dict()
    context["levels"] = {
        "1": {"name": "easy",       "value": "1"},
        "2": {"name": "normal",     "value": "2"},
        "3": {"name": "hard",       "value": "3"},
        "4": {"name": "expert",     "value": "4"},
        "5": {"name": "extreme",    "value": "5"}
    }
    try:
        context["difficulty"] = request.session.get("difficulty")
        context["username"] = request.session.get("username")
        context["authorized"] = request.session.get("authorized")
        context["dif_choice"] = context["levels"][context["difficulty"]]
    except:
        request.session["difficulty"] = "3"
        if context["authorized"] == True:
            return render(request, "games/games.html", context)
        else:
            return HttpResponseRedirect(reverse("login"))

    if request.POST:
        context["difficulty"] = request.POST["difficulty"]
        context["dif_choice"] = context["levels"][context["difficulty"]]
        request.session["difficulty"] = context["dif_choice"]["value"]
        print(request.session["difficulty"])
        if context["authorized"] == True:
            return render(request, "games/games.html", context)
    else:
        if context["authorized"] == True:
            return render(request, "games/games.html", context)
        else:
            return HttpResponseRedirect(reverse("login"))

 
def guess_game(request):
    context = dict()
    context["authorized"] = request.session.get("authorized")
    context["username"] = request.session.get("username")
    context["diff_int"] = int(request.session["difficulty"])
    context["diff_str"] = request.session["difficulty"]
    context["game_name"] = "guess_game"
    context["game_status"] = "loose"

    if context["authorized"]:
        if request.POST:
            try:
                users_value = int(request.POST["guess"])
                random_value = int(request.session.get("generated_number"))
                request.session["generated_number"] = None
                if users_value == random_value:
                    context["game_status"] = "win"
                    user = get_user(context["username"])
                    user.score += context["diff_int"] * 3 + 5
                    user.save()
                    print(user.score)
                    return render(request, "games/endgame.html", context)
                else:
                    context["game_status"] = "loose"
                    return render(request, "games/endgame.html", context)
            except:
                request.session["generated_number"] = random.randint(0, context["diff_int"])
                new = request.session.get("generated_number")
                print(new)
                return render(request, "games/guess-game.html", context)

        request.session["generated_number"] = random.randint(0, context["diff_int"])
        new = request.session.get("generated_number")
        print(new)
        return render(request, "games/guess-game.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def currency_roulette_game(request):
    context = dict()
    context["authorized"] = request.session.get("authorized")
    context["username"] = request.session.get("username")
    context["diff_int"] = int(request.session["difficulty"])
    context["diff_str"] = request.session["difficulty"]
    context["game_name"] = "roulette_game"
    context["game_status"] = "loose"
    context["usd_amount"] = random.randint(1,100)
    min, max = get_money_interval(context["usd_amount"], context["diff_int"])
    print(min, max)
    if context["authorized"]:
        if request.POST:
            try:
                min_value = request.session.get("min")
                max_value = request.session.get("max")
                users_value = request.POST["guess"]
                request.session["min"] = None
                request.session["max"] = None
                if isfloat(users_value) and min_value <= float(users_value) <= max_value:
                    context["game_status"] = "win"
                    user = get_user(context["username"])
                    user.score += context["diff_int"] * 3 + 5
                    user.save()
                    print(user.score)
                    return render(request, "games/endgame.html", context)
                else:
                    context["game_status"] = "loose"
                    return render(request, "games/endgame.html", context)
            except:
                pass

        request.session["min"] = min
        request.session["max"] = max
        return render(request, "games/currency-roulette-game.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))


def memory_game(request):
    context = dict()
    min_value = 1
    max_value = 101
    context["authorized"] = request.session.get("authorized")
    context["username"] = request.session.get("username")
    context["diff_int"] = int(request.session["difficulty"])
    context["diff_str"] = request.session["difficulty"]
    context["game_name"] = "memory_game"
    context["game_status"] = "loose"
    if context["authorized"]:
        if request.POST:
            random_vlues = request.session["randsequence"]
            request.session["randsequence"] = None
            user_values = []
            for form in request.POST:
                user_values.append(request.POST[form])
            user_values = user_values[1:]
            print(user_values)
            if  user_values == random_vlues:
                context["game_status"] = "win"
                user = get_user(context["username"])
                user.score += context["diff_int"] * 3 + 5
                user.save()
                print(user.score)
                return render(request, "games/endgame.html", context)
            else:
                context["game_status"] = "loose"
                return render(request, "games/endgame.html", context)
                
        context["randsequence"] = [str(random.randint(min_value, max_value)) for _ in range(context["diff_int"])]
        request.session["randsequence"] = context["randsequence"]
        print(context["randsequence"])
        return render(request, "games/memory-game.html", context)
    else:
        return HttpResponseRedirect(reverse("login"))
 