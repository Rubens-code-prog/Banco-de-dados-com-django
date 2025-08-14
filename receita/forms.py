from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'ingredientes', 'modo_preparo', 'categoria']
    
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo'].strip()

        if len(titulo) < 3:
            raise forms.ValidationError('O titulo precisa ter pelo menos 3 caracteres.')
        
        return titulo