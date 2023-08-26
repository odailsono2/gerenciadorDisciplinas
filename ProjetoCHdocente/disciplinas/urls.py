from django.urls import path
from . import views

urlpatterns = [
    path('listarDisciplinasBD/', views.ListarDisciplinasBD, name='ListarDisciplinasBD'),
    path('carregarxls/', views.carrega_xls, name='carregar_xls'),
]