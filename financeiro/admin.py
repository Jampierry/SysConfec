from django.contrib import admin
from .models import Categoria, Lancamento
from SysConfec_app import brl

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('nome',)

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'valor_brl', 'categoria', 'tipo')
    list_filter = ('tipo', 'categoria')
    search_fields = ('descricao',)

    def valor_brl(self, obj):
        return brl(obj.valor)
    valor_brl.short_description = 'Valor'
