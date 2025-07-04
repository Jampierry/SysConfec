from django.db import models

# Create your models here.

class Parametro(models.Model):
    chave = models.CharField(max_length=100, unique=True)
    valor = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.chave
