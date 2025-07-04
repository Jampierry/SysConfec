from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def cadastro_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if not username or not password or not password2:
            messages.error(request, 'Preencha todos os campos.')
        elif password != password2:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Usuário criado com sucesso! Faça login.')
            return redirect(reverse('login'))
    return render(request, 'usuarios/cadastro.html')
