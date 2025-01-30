from django.shortcuts import render

def contato(request):
    return render(request, 'cadastro/contato.html')
from .models import Aluno

# Função para listar alunos
def lista_alunos(request):
    alunos = Aluno.objects.all()  # Pega todos os alunos cadastrados
    return render(request, 'cadastro/alunos.html', {'alunos': alunos})
