from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Parametro
from django.views.decorators.http import require_POST
import subprocess
import sys

# Create your views here.

# View principal de configurações

def configuracoes_home(request):
    exibir_ficticio = Parametro.objects.filter(chave='exibir_dados_ficticios').first()
    context = {
        'exibir_ficticio': exibir_ficticio.valor == 'True' if exibir_ficticio else False
    }
    return render(request, 'configuracoes/home.html', context)

@require_POST
def gerar_dados_ficticios(request):
    try:
        result = subprocess.run([
            sys.executable, 'scripts_git/popula_ficticio.py'
        ], capture_output=True, text=True, check=True)
        messages.success(request, 'Dados fictícios gerados com sucesso!\n' + result.stdout)
    except subprocess.CalledProcessError as e:
        messages.error(request, f'Erro ao gerar dados fictícios: {e}\n{e.stderr}')
    except Exception as e:
        messages.error(request, f'Erro inesperado: {e}')
    return redirect('configuracoes_home')

@require_POST
def remover_dados_ficticios(request):
    try:
        result = subprocess.run([
            sys.executable, 'scripts_git/popula_ficticio.py', 'remover'
        ], capture_output=True, text=True, check=True)
        messages.success(request, 'Dados fictícios removidos com sucesso!\n' + result.stdout)
    except subprocess.CalledProcessError as e:
        messages.error(request, f'Erro ao remover dados fictícios: {e}\n{e.stderr}')
    except Exception as e:
        messages.error(request, f'Erro inesperado: {e}')
    return redirect('configuracoes_home')

@require_POST
def alternar_exibicao_ficticio(request):
    exibir = request.POST.get('exibir_ficticio') == 'on'
    Parametro.objects.update_or_create(
        chave='exibir_dados_ficticios',
        defaults={'valor': str(exibir), 'descricao': 'Exibir dados fictícios no sistema'}
    )
    messages.success(request, f'Exibição de dados fictícios: {"ativada" if exibir else "desativada"}.')
    return redirect('configuracoes_home')
