from django.db import models
from SysConfec_app import brl

# Create your models here.

class Categoria(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

class Lancamento(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='lancamentos')
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255, blank=True)
    comprovante = models.FileField(upload_to='comprovantes/', blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=Categoria.TIPO_CHOICES)
    ordem_producao = models.ForeignKey('ordens.OrdemProducao', on_delete=models.SET_NULL, null=True, blank=True, related_name='lancamentos')
    funcionario = models.ForeignKey('funcionarios.Funcionario', on_delete=models.SET_NULL, null=True, blank=True, related_name='lancamentos')

    def __str__(self):
        return f"{self.data} - {self.categoria} - {brl(self.valor)}"
