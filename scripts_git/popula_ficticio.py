import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import django
from datetime import datetime, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SysConfec_app.settings')
django.setup()

from funcionarios.models import Cargo, Funcionario
from ordens.models import OrdemProducao
from financeiro.models import Categoria, Lancamento
from configuracoes.models import Parametro
from django.contrib.auth.models import User

# Parâmetros
DATA_INICIO = datetime(2025, 1, 1)
DATA_FIM = datetime(2025, 8, 30)
QTD_MESES = (DATA_FIM.year - DATA_INICIO.year) * 12 + (DATA_FIM.month - DATA_INICIO.month) + 1
QTD_LANCAMENTOS = 20

# Dados base
CARGOS = [
    ('Costureira', 'Responsável pela costura', 2200),
    ('Cortador', 'Responsável pelo corte', 2000),
    ('Supervisor', 'Supervisiona a produção', 3000),
    ('Auxiliar', 'Apoio geral', 1500),
]
FUNCIONARIOS = [
    'Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique', 'Isabela', 'João',
    'Katia', 'Lucas', 'Marina', 'Natan', 'Olivia', 'Paulo', 'Quésia', 'Rafael', 'Sabrina', 'Tiago'
]
CATEGORIAS_RECEITA = ['Venda Loja', 'Venda Online', 'Comissão', 'Outros']
CATEGORIAS_DESPESA = ['Insumos', 'Energia', 'Água', 'Manutenção', 'Transporte', 'Salários']
PRODUTOS = ['Legging', 'Top', 'Camiseta', 'Short', 'Jaqueta', 'Macacão']
MARCAS = ['FitPro', 'ActiveWear', 'PowerGym', 'MoveIt']

# Funções auxiliares
def random_date(month, year):
    day = random.randint(1, 28)
    return datetime(year, month, day)

def criar_dados_ficticios():
    # Cargos
    cargos_objs = []
    for nome, desc, salario in CARGOS:
        obj, _ = Cargo.objects.get_or_create(nome=nome, defaults={'descricao': desc, 'salario_base': salario})
        cargos_objs.append(obj)
    # Funcionários
    for i, nome in enumerate(FUNCIONARIOS):
        cargo = random.choice(cargos_objs)
        Funcionario.objects.get_or_create(
            nome=nome,
            defaults={
                'cargo': cargo,
                'salario': cargo.salario_base,
                'contato': f'{nome.lower()}@sysconfec.local',
                'data_admissao': DATA_INICIO.date(),
                'ativo': True
            }
        )
    # Categorias
    for cat in CATEGORIAS_RECEITA:
        Categoria.objects.get_or_create(nome=cat, tipo='receita')
    for cat in CATEGORIAS_DESPESA:
        Categoria.objects.get_or_create(nome=cat, tipo='despesa')
    # Ordens de Produção e Lançamentos
    for mes in range(QTD_MESES):
        ano = DATA_INICIO.year + (DATA_INICIO.month + mes - 1) // 12
        mes_atual = (DATA_INICIO.month + mes - 1) % 12 + 1
        for i in range(QTD_LANCAMENTOS):
            produto = random.choice(PRODUTOS)
            marca = random.choice(MARCAS)
            referencia = f"OP{ano}{mes_atual:02d}{i:03d}"
            data_inicio = random_date(mes_atual, ano)
            data_fim = data_inicio + timedelta(days=random.randint(2, 10))
            status = random.choice(['andamento', 'finalizado', 'pendente'])
            quantidade = random.randint(50, 300)
            ordem = OrdemProducao.objects.create(
                referencia=referencia,
                produto=produto,
                marca=marca,
                data_inicio=data_inicio.date(),
                data_fim=data_fim.date(),
                status=status,
                quantidade=quantidade,
                grade_p=random.randint(0, quantidade//5),
                grade_m=random.randint(0, quantidade//5),
                grade_g=random.randint(0, quantidade//5),
                grade_gg=random.randint(0, quantidade//5),
                grade_eg=random.randint(0, quantidade//5),
                observacoes='Ordem fictícia.'
            )
            # Lançamentos financeiros
            for _ in range(2):
                tipo = random.choice(['receita', 'despesa'])
                if tipo == 'receita':
                    categoria = Categoria.objects.filter(tipo='receita').order_by('?').first()
                    valor = random.randint(1000, 5000)
                else:
                    categoria = Categoria.objects.filter(tipo='despesa').order_by('?').first()
                    valor = random.randint(500, 3000)
                funcionario = Funcionario.objects.order_by('?').first()
                Lancamento.objects.create(
                    categoria=categoria,
                    data=data_inicio.date(),
                    valor=valor,
                    descricao=f'Lançamento fictício {referencia}',
                    tipo=tipo,
                    ordem_producao=ordem,
                    funcionario=funcionario
                )
    # Parâmetro para controle de exibição
    Parametro.objects.update_or_create(
        chave='exibir_dados_ficticios',
        defaults={'valor': 'True', 'descricao': 'Exibir dados fictícios no sistema'}
    )
    print('Dados fictícios criados com sucesso!')

def remover_dados_ficticios():
    # Remover lançamentos fictícios
    lanc_del = Lancamento.objects.filter(descricao__icontains='fictício')
    print(f'Removendo {lanc_del.count()} lançamentos fictícios')
    lanc_del.delete()
    # Remover ordens fictícias
    ord_del = OrdemProducao.objects.filter(observacoes__icontains='fictícia')
    print(f'Removendo {ord_del.count()} ordens fictícias')
    ord_del.delete()
    # Remover funcionários fictícios
    func_del = Funcionario.objects.filter(contato__icontains='@sysconfec.local')
    print(f'Removendo {func_del.count()} funcionários fictícios')
    func_del.delete()
    # Remover categorias fictícias
    cat_del = Categoria.objects.filter(nome__in=CATEGORIAS_RECEITA + CATEGORIAS_DESPESA)
    print(f'Removendo {cat_del.count()} categorias fictícias')
    cat_del.delete()
    # Remover cargos fictícios
    cargo_del = Cargo.objects.filter(nome__in=[c[0] for c in CARGOS])
    print(f'Removendo {cargo_del.count()} cargos fictícios')
    cargo_del.delete()
    # Remover parâmetro
    param_del = Parametro.objects.filter(chave='exibir_dados_ficticios')
    print(f'Removendo {param_del.count()} parâmetro de exibição')
    param_del.delete()
    print('Dados fictícios removidos com sucesso!')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'remover':
        remover_dados_ficticios()
    else:
        criar_dados_ficticios() 