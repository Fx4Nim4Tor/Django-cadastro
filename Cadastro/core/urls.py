from django.urls import path
from core import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
]