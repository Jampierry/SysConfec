from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Ajuste para o nome da sua view de dashboard

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect(reverse('login'))
