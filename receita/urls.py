from django.urls import path
from . import views

urlpatterns = [
    path('receitas/', views.receitas, name='receitas'),
    path('detalhes_receita/<int:id_receita>/', views.detalhes_receita, name='detalhes_receita'),
]