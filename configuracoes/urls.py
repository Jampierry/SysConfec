from django.urls import path
from .views import configuracoes_home, gerar_dados_ficticios, remover_dados_ficticios, alternar_exibicao_ficticio

urlpatterns = [
    path('', configuracoes_home, name='configuracoes_home'),
    path('gerar-ficticio/', gerar_dados_ficticios, name='gerar_dados_ficticios'),
    path('remover-ficticio/', remover_dados_ficticios, name='remover_dados_ficticios'),
    path('alternar-ficticio/', alternar_exibicao_ficticio, name='alternar_exibicao_ficticio'),
] 