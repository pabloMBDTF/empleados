from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import prueba

class IndexView(TemplateView):
    template_name = 'home/home.html'


class lista(ListView):
    template_name = 'home/listas.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'


class ModeloLista (ListView):
    template_name = 'home/prueba.html'
    model = prueba
    context_object_name = 'listaPrueba'

