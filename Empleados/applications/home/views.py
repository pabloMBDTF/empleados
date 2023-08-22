from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import prueba
from .forms import PruebaForm

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

class add (CreateView):
    model = prueba
    template_name = 'home/añadir.html'
    success_url = '.'
    form_class = PruebaForm
