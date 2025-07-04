from django.db import models
from SysConfec_app import brl

# Create your models here.

class OrdemProducao(models.Model):
    STATUS_CHOICES = [
        ('andamento', 'Em andamento'),
        ('finalizado', 'Finalizado'),
        ('pendente', 'Pendente'),
        ('cancelado', 'Cancelado'),
    ]
    referencia = models.CharField(max_length=50, unique=True)
    produto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='andamento')
    quantidade = models.PositiveIntegerField()
    grade_p = models.PositiveIntegerField(default=0)
    grade_m = models.PositiveIntegerField(default=0)
    grade_g = models.PositiveIntegerField(default=0)
    grade_gg = models.PositiveIntegerField(default=0)
    grade_eg = models.PositiveIntegerField(default=0)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.referencia} - {self.produto} - {self.marca}"
