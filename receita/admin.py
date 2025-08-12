from django.contrib import admin
from .models import Categoria, Receita

# Register your models here.
class Receitas(admin.ModelAdmin):
    list_display = ['titulo', 'categoria']
    search_fields = ['titulo']
    list_filter = ['categoria', 'data_criacao']

admin.site.register(Categoria)
admin.site.register(Receita, Receitas)