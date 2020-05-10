from django.contrib import admin
from .models import Partida, Jogadores, Noticias

# Partida
class PartidaAdmin(admin.ModelAdmin):
	list_display = ['nome']
	search_fields = ['nome']

admin.site.register(Partida, PartidaAdmin)

# Jogadores
class JogadoresAdmin(admin.ModelAdmin):
	list_display = ['nome', 'conta', 'saldo', 'partida']
	search_fields = ['nome']

admin.site.register(Jogadores, JogadoresAdmin)

# Notícias
class NoticiasAdmin(admin.ModelAdmin):
	list_display = ['titulo', 'noticia']
	search_fields = ['titulo', 'noticia']

admin.site.register(Noticias, NoticiasAdmin)