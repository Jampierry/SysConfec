# SysConfec

Sistema Django para controle de facção de costura.

## Estrutura do Projeto

- **SysConfec_app/**: App principal, configurações, filtros customizados (templatetags), urls globais.
- **funcionarios/**: CRUD de funcionários, cargos, templates modernos.
- **ordens/**: CRUD de ordens de produção.
- **financeiro/**: CRUD de receitas, despesas, contas, categorias.
- **configuracoes/**: Tela de configurações, scripts de dados fictícios, seletor de tema.
- **usuarios/**: Cadastro, edição, exclusão de usuários.
- **login/**: Tela de login customizada.
- **templates/**: Templates centralizados, todos estendem `base.html`.
- **static/**: CSS, imagens, ícones.
- **HISTORICO_CHAT/**: Histórico de conversas e decisões do projeto.

## Funcionalidades

- Dashboard moderno com cards e gráficos dinâmicos (Chart.js).
- Menu lateral retrátil, azul, com ícones, responsivo e consistente em todas as telas.
- CRUD completo para Funcionários, Ordens, Financeiro, Usuários.
- Filtros customizados para moeda brasileira (`brl`) e menu ativo (`startswith`).
- Proteção de rotas por login.
- Cadastro de usuário via interface.
- Geração/remoção de dados fictícios via interface e script.
- Layout limpo, responsivo, UX moderna.

## Padrões e Boas Práticas

- Todos os templates estendem `base.html`.
- Menu lateral único, sem duplicação de código.
- Filtros customizados em `SysConfec_app/templatetags`.
- Estrutura modular de apps.
- Código limpo, sem arquivos ou migrations desnecessários.

## Desenvolvimento

1. Clone o repositório e crie um ambiente virtual.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Rode as migrations: `python manage.py migrate`.
4. Crie um superusuário: `python manage.py createsuperuser`.
5. Inicie o servidor: `python manage.py runserver`.

## Deploy

- Use um servidor WSGI/ASGI para produção.
- Configure variáveis de ambiente e banco de dados seguro.
- Atualize o repositório no GitHub após cada alteração relevante.

## Histórico de Conversas

- Os registros de decisões e conversas estão em `HISTORICO_CHAT/`.

---

Para dúvidas, consulte o código ou o histórico de chat. 