#!/bin/bash
# Script para comitar e subir todas as alterações do projeto SysConfec para o GitHub

# Mensagem de commit padrão ou passada como argumento
MENSAGEM_COMMIT=${1:-"Atualização automática do projeto SysConfec"}

echo "Adicionando todos os arquivos..."
git add .

echo "Fazendo commit..."
git commit -m "$MENSAGEM_COMMIT"

echo "Enviando para o repositório remoto..."
git push origin main

echo "Projeto SysConfec atualizado no GitHub!" 