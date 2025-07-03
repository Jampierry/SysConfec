from django.db import models
from funcionarios.models import Funcionario

class OrdemProducao(models.Model):
    """
    Representa uma ordem de produção na facção de costura.
    """
    STATUS_CHOICES = [
        ("em_andamento", "Em andamento"),
        ("finalizada", "Finalizada"),
        ("pendente", "Pendente"),
        ("cancelada", "Cancelada"),
    ]

    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_entrega = models.DateField(verbose_name="Data de Entrega Prevista")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade a Produzir")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="em_andamento", verbose_name="Status")
    funcionario_responsavel = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name="ordens_responsaveis", verbose_name="Responsável")
    data_finalizacao = models.DateField(null=True, blank=True, verbose_name="Data de Finalização")

    def __str__(self):
        return f"Ordem #{self.id} - {self.descricao}"

    class Meta:
        verbose_name = "Ordem de Produção"
        verbose_name_plural = "Ordens de Produção"
        ordering = ["-data_inicio"] 