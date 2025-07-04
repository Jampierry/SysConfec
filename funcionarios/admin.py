from django.contrib import admin
from .models import Cargo, Funcionario
from SysConfec_app import brl

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'salario_base_brl')
    search_fields = ('nome',)

    def salario_base_brl(self, obj):
        return brl(obj.salario_base)
    salario_base_brl.short_description = 'Salário Base'

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'salario_brl', 'ativo')
    list_filter = ('cargo', 'ativo')
    search_fields = ('nome', 'cargo__nome')

    def salario_brl(self, obj):
        return brl(obj.salario)
    salario_brl.short_description = 'Salário'
