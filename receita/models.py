from django.db import models
from django.contrib.auth.models import User

    
class Receita(models.Model):
    titulo = models.CharField(max_length=70, blank=False)
    descricao = models.TextField(max_length=200)
    tempo_preparacao = models.IntegerField()
    serve_pessoas = models.IntegerField()
    serve_porcoes = models.CharField(max_length=60)
    publicada = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='imagens', blank=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

