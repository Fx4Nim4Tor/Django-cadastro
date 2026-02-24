from django.shortcuts import render
from core.services.cria_usuarios import Cria_usuarios


def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        Cria_usuarios(nome, email, senha)
    return render(request, "core/cadastro.html")