from django.shortcuts import render
from .models import Partida, Jogadores, Noticias

def partidas(request):
	dados = {
		'Partidas': Partida.objects.all()
	}
	return render(request, 'index.html', dados)

def jogadores(request, id_partida):
	dados = {
		'Jogadores': Jogadores.objects.filter(partida=id_partida)
	}
	return render(request, 'jogadores.html', dados)

def conta(request, id, id_partida):

	dados = {
		'Jogadores': Jogadores.objects.filter(partida=id_partida),
		'Jogador': Jogadores.objects.get(conta=id),
		'Noticia': Noticias.objects.order_by("?").first()
	}
	return render(request, 'conta.html', dados)

def receber(request, id, id_partida, valor):
	jogador = Jogadores.objects.get(conta=id)
	jogador.saldo = jogador.saldo + valor

	jogador.save()

	dados = {
		'Jogadores': Jogadores.objects.filter(partida=id_partida),
		'Jogador': jogador,
		'Noticia': Noticias.objects.order_by("?").first()
	}
	return render(request, 'conta.html', dados)

def sacar(request, id, id_partida, valor):
	jogador = Jogadores.objects.get(conta=id)
	jogador.saldo = jogador.saldo - valor

	jogador.save()

	dados = {
		'Jogadores': Jogadores.objects.filter(partida=id_partida),
		'Jogador': jogador,
		'Noticia': Noticias.objects.order_by("?").first()
	}

	return render(request, 'conta.html', dados)

def transferir(request, id, id_partida, valor, id_favorecido):
	Pagador = Jogadores.objects.get(conta=id)
	Pagador.saldo = Pagador.saldo - valor
	Pagador.save()

	Favorecido = Jogadores.objects.get(conta=id_favorecido)
	Favorecido.saldo = Favorecido.saldo + valor
	Favorecido.save()

	dados = {
		'Jogadores': Jogadores.objects.filter(partida=id_partida),
		'Jogador': Pagador,
		'Noticia': Noticias.objects.order_by("?").first()
	}

	return render(request, 'conta.html', dados)