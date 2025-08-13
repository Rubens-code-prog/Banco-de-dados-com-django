from django.shortcuts import render
from .models import Receita

# Create your views here.
def receitas(request):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}

    return render(request, 'minhas_receitas.html', context)