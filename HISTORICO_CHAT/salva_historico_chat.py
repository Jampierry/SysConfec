import os
import shutil
from datetime import datetime

# Caminhos absolutos
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ORIGEM = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'SGFP-SYSTEM', 'system', 'CHAT_CURSOR_AI'))
DESTINO = BASE_DIR

# Garante que o destino existe
os.makedirs(DESTINO, exist_ok=True)

# Lista todos os arquivos de histórico do chat
if not os.path.exists(ORIGEM):
    print(f"A pasta de origem {ORIGEM} não existe.")
else:
    for nome_arquivo in os.listdir(ORIGEM):
        if nome_arquivo.startswith('conversa_cursor_') and nome_arquivo.endswith('.txt'):
            caminho_origem = os.path.join(ORIGEM, nome_arquivo)
            try:
                partes = nome_arquivo.replace('.txt', '').split('_')
                data_str = partes[-1]  # Ex: 2025-07-03
                # Usa a data do arquivo + hora de modificação
                data_mod = datetime.fromtimestamp(os.path.getmtime(caminho_origem))
                nome_destino = f"chat_{data_str} - {data_mod.strftime('%H-%M')}.txt"
                caminho_destino = os.path.join(DESTINO, nome_destino)
                if not os.path.exists(caminho_destino):
                    shutil.copy2(caminho_origem, caminho_destino)
                    print(f"Copiado: {nome_arquivo} -> {nome_destino}")
                else:
                    print(f"Já existe: {nome_destino}")
            except Exception as e:
                print(f"Erro ao processar {nome_arquivo}: {e}")