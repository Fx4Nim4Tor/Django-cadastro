from django.shortcuts import render, redirect
from django.contrib import messages
from core.services.cria_usuarios import Cria_usuarios


def login(request):
    """Página inicial após cadastro com sucesso."""
    return render(request, "core/inicio.html")


def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        # print(nome, email, senha)
        valida = Cria_usuarios(nome, email, senha)
        if valida['success']:
            messages.success(request, f"Bem-vindo, {nome}! Cadastro realizado com sucesso!")
            return redirect('login')
        else:
            error_msg = valida.get('message', 'Erro ao cadastrar.')
            messages.error(request, f"Erro: {error_msg}")
            
    return render(request, "core/cadastro.html")


