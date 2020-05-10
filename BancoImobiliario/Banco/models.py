from django.db import models

# Create your models here.
class Partida(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Jogadores(models.Model):
    conta = models.AutoField(primary_key=True)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    saldo = models.FloatField()

    def __str__(self):
        return self.nome

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    noticia = models.TextField()

    def __str__(self):
        return self.titulo