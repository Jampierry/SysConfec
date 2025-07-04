"""
URL configuration for SysConfec_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from funcionarios.models import Funcionario
from financeiro.models import Lancamento
from ordens.models import OrdemProducao
from configuracoes.utils import exibir_dados_ficticios
from django.db import models

# View simples de dashboard protegida por login
@login_required
def dashboard_view(request):
    # Filtro de exibição de dados fictícios
    if exibir_dados_ficticios():
        funcionarios = Funcionario.objects.exclude(email__icontains='@sysconfec.local', ativo=False)
        ordens = OrdemProducao.objects.all()
        lancamentos = Lancamento.objects.all()
    else:
        funcionarios = Funcionario.objects.exclude(email__icontains='@sysconfec.local')
        ordens = OrdemProducao.objects.exclude(observacoes__icontains='fictícia')
        lancamentos = Lancamento.objects.exclude(descricao__icontains='fictício')
    receita_mes = lancamentos.filter(tipo='receita').aggregate(total=models.Sum('valor'))['total'] or 0
    despesa_mes = lancamentos.filter(tipo='despesa').aggregate(total=models.Sum('valor'))['total'] or 0
    ordens_andamento = ordens.filter(status='andamento').count()
    funcionarios_ativos = funcionarios.filter(ativo=True).count()
    # Dados para o gráfico
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto']
    receitas_por_mes = []
    despesas_por_mes = []
    for i, mes_nome in enumerate(meses, 1):
        receitas_por_mes.append(lancamentos.filter(tipo='receita', data__month=i).aggregate(total=models.Sum('valor'))['total'] or 0)
        despesas_por_mes.append(lancamentos.filter(tipo='despesa', data__month=i).aggregate(total=models.Sum('valor'))['total'] or 0)
    context = {
        'receita_mes': receita_mes,
        'despesa_mes': despesa_mes,
        'ordens_andamento': ordens_andamento,
        'funcionarios_ativos': funcionarios_ativos,
        'meses': meses,
        'receitas_por_mes': receitas_por_mes,
        'despesas_por_mes': despesas_por_mes,
    }
    return render(request, 'dashboard.html', context)

def home_redirect(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('funcionarios.urls')),
    path('ordens/', include('ordens.urls')),
    path('financeiro/', include('financeiro.urls')),
    path('configuracoes/', include('configuracoes.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('login/', include('login.urls')),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', home_redirect, name='home'),
]
