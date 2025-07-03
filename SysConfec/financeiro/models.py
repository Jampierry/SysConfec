from django.db import models

class CategoriaFinanceira(models.Model):
    """
    Representa uma categoria financeira para receitas ou despesas.
    Exemplo: Venda de Peças, Insumos, Energia, Transporte, etc.
    """
    TIPO_CHOICES = [
        ("receita", "Receita"),
        ("despesa", "Despesa"),
    ]
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome da Categoria")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, verbose_name="Tipo")
    descricao = models.TextField(blank=True, verbose_name="Descrição")

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

    class Meta:
        verbose_name = "Categoria Financeira"
        verbose_name_plural = "Categorias Financeiras"
        ordering = ["tipo", "nome"]

class LancamentoFinanceiro(models.Model):
    """
    Representa um lançamento financeiro (receita ou despesa) no sistema.
    """
    valor = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Valor")
    data = models.DateField(verbose_name="Data do Lançamento")
    categoria = models.ForeignKey(CategoriaFinanceira, on_delete=models.PROTECT, related_name="lancamentos", verbose_name="Categoria")
    descricao = models.CharField(max_length=200, blank=True, verbose_name="Descrição")
    comprovante = models.FileField(upload_to="comprovantes/", blank=True, null=True, verbose_name="Comprovante (opcional)")

    def __str__(self):
        return f"{self.categoria.nome} - {self.valor} em {self.data}"

    class Meta:
        verbose_name = "Lançamento Financeiro"
        verbose_name_plural = "Lançamentos Financeiros"
        ordering = ["-data", "-id"] 