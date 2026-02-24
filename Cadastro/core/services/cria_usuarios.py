from django.shortcuts import redirect
from core.models import Usuario

def Cria_usuarios(nome, email, senha):
        Usuario.objects.create(
            nome=nome,
            email=email,
            senha=senha
        )

        return redirect("/cadastro/")