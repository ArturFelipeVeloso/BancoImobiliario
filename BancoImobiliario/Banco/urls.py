from django.contrib import admin
from django.urls import path
from .views import partidas, jogadores, conta, receber, sacar, transferir
urlpatterns = [
    path('', partidas),
	path('<int:id_partida>/jogadores/', jogadores),
	path('<int:id_partida>/jogadores/<int:id>/conta/', conta),
	path('<int:id_partida>/jogadores/<int:id>/conta/depositar/<int:valor>', receber),
	path('<int:id_partida>/jogadores/<int:id>/conta/sacar/<int:valor>', sacar),
	path('<int:id_partida>/jogadores/<int:id>/conta/transferir/<int:valor>/<int:id_favorecido>', transferir),
]
