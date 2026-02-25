import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
import django
django.setup()
from core.services.cria_usuarios import Cria_usuarios
print(Cria_usuarios('TesteX','testex@example.com','senha123'))
