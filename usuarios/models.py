from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Exemplo de extensão do modelo User para perfil customizado
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True)
    # Adicione outros campos de perfil conforme necessário

    def __str__(self):
        return self.user.username
