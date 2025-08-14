from django.shortcuts import render
from .models import Receita

# Create your views here.
def receitas(request):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}

    return render(request, 'minhas_receitas.html', context)

def detalhes_receita(request, id_receita):
    receita = Receita.objects.get(id=id_receita)
    context = {'receita': receita}

    return render(request, 'detalhes_receita.html', context)