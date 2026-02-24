from django.urls import path
from core import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
]