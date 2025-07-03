from django.db import models

class Cargo(models.Model):
    """
    Representa um cargo/função dentro da facção de costura.
    Exemplo: Costureiro, Supervisor, Auxiliar, etc.
    """
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome do Cargo")
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salário Base")
    descricao = models.TextField(blank=True, verbose_name="Descrição do Cargo")

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    """
    Representa um funcionário da facção de costura.
    """
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name="funcionarios", verbose_name="Cargo")
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salário Atual")
    telefone = models.CharField(max_length=20, blank=True, verbose_name="Telefone")
    email = models.EmailField(blank=True, verbose_name="E-mail")
    data_admissao = models.DateField(verbose_name="Data de Admissão")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ["nome"] 