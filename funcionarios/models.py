from django.db import models
from SysConfec_app import brl

# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {brl(self.salario_base)}"

class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='funcionarios')
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    contato_emergencia = models.CharField(max_length=100, blank=True)
    data_admissao = models.DateField()
    data_demissao = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.cargo.nome} - {brl(self.salario)}"
