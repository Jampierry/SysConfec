#!/bin/bash
# Script para commit inicial do projeto SysConfec

echo "# SysConfec" >> README.md

git init
git add README.md
git commit -m "Comit Inicial"
git branch -M main
git remote add origin https://github.com/Jampierry/SysConfec.git
git push -u origin main

echo "Commit inicial realizado e projeto enviado para o GitHub!" 