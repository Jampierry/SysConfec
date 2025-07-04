from django.contrib import admin
from .models import OrdemProducao

@admin.register(OrdemProducao)
class OrdemProducaoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'produto', 'marca', 'status', 'data_inicio', 'data_fim')
    list_filter = ('status', 'marca')
    search_fields = ('referencia', 'produto', 'marca')
