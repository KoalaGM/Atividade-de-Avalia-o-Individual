from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),  # Página que lista os alunos
    path('contato/', views.contato, name='contato'),  # Página de contato
]
