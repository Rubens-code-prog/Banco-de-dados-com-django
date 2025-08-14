from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Receita
from .forms import ReceitaForm

# Create your views here.
def receitas(request):
    receitas = Receita.objects.all()
    context = {'receitas': receitas}

    return render(request, 'minhas_receitas.html', context)

def detalhes_receita(request, id_receita):
    receita = Receita.objects.get(id=id_receita)
    context = {'receita': receita}

    return render(request, 'detalhes_receita.html', context)

def nova_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita cadastrada com sucesso!')
            return redirect('receitas')
    else:
        form = ReceitaForm()
    return render(request, 'nova_receita.html', {'form': form})

def editar_receita(request, id_receita):
    receita = get_object_or_404(Receita, id=id_receita)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita editada')
            return redirect('receitas')
    else:
        form = ReceitaForm(instance=receita)
    return render(request, 'nova_receita.html', {'form': form, 'editar': True})