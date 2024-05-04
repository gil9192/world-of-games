from django.urls import path
from . import views


urlpatterns = [
    path('', views.games, name="games"),
    path('guess/', views.guess_game, name="guess"),
    path('memory/', views.memory_game, name="memory"),
    path('roulette/', views.currency_roulette_game, name="roulette")
]
