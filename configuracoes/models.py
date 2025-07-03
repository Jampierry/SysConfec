from django.db import models

# Create your models here.

class ConfiguracaoSistema(models.Model):
    """
    Armazena parâmetros e configurações gerais do sistema.
    Exemplo: moeda padrão, notificações, parâmetros de backup, etc.
    """
    chave = models.CharField(max_length=50, unique=True, verbose_name="Chave de Configuração")
    valor = models.CharField(max_length=200, verbose_name="Valor")
    descricao = models.TextField(blank=True, verbose_name="Descrição da Configuração")

    def __str__(self):
        return f"{self.chave}: {self.valor}"

    class Meta:
        verbose_name = "Configuração do Sistema"
        verbose_name_plural = "Configurações do Sistema"
        ordering = ["chave"]
