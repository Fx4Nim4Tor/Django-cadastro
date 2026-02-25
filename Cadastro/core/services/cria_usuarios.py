from django.shortcuts import redirect
from core.models import Usuario
from django.contrib.auth.hashers import make_password
from django.db import DatabaseError, IntegrityError
from django.db import transaction


def Cria_usuarios(nome, email, senha):
	"""Cria e salva um `Usuario` usando o ORM do Django.

	Faz hash da senha com `make_password` e salva, retornando a instância.
	"""
	try:
		if Usuario.objects.filter(email=email).exists():
			return {
				'success': False,
				'error': 'email_exists',
				'message': 'Email já cadastrado.'
			}

		with transaction.atomic():
			usuario = Usuario(
				nome=nome,
				email=email,
				senha=make_password(senha)
			)
			usuario.save()
		return {
			'success': True,
			'usuario': usuario
		}
	except IntegrityError as e:
		return {
			'success': False,
			'error': 'integrity_error',
			'message': str(e)
		}
	except DatabaseError as e:
		return {
			'success': False,
			'error': 'db_error',
			'message': 'Erro ao acessar o banco de dados.',
			'detail': str(e)
		}


