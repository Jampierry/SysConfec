from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Usuário do sistema com controle de permissões (admin ou comum).
    """
    TIPO_CHOICES = [
        ("admin", "Administrador"),
        ("comum", "Usuário Comum"),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default="comum", verbose_name="Tipo de Usuário")

    def is_admin(self):
        """Retorna True se o usuário for administrador."""
        return self.tipo == "admin" or self.is_superuser

    def __str__(self):
        return self.get_full_name() or self.username

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["username"] 