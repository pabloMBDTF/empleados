from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.template import Context
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

from .models import Empleado

# 1. listar todos los empleados de la empresa - r
# 2. lisrtar empleados por area - r
# 3. listar por trabajo -nr
# 4. lisrtar por palabra clave -
# 5. lisrtar por habilidades


class ListAllEmpleados(ListView):
    template_name = 'empleados/empleadosLista.html'
    context_object_name = 'lista'
    paginate_by = 4
    ordering = 'firstName'

    def get_queryset(self):
        palabraClave = self.request.GET.get("keyword", " ")
        lista = Empleado.objects.filter(
            nombreCompleto__icontains = palabraClave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'empleados/empleadosAdmin.html'
    paginate_by = 10
    context_object_name = 'empleados'
    ordering = 'firstName'
    model = Empleado




    

# listar por filtro

#area
class ListarPorArea(ListView):
    template_name = 'empleados/listByArea.html'
    context_object_name = 'empAreas'
    
    def get_queryset(self):
        # de esta manera se trae el parametro de el enlace 
        
        area = str(self.kwargs['shortName'])
        lista = Empleado.objects.filter(
            departamento__shortName = area
        )
        
        return lista
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area = str(self.kwargs['shortName'])
        context['Area'] = area
        return context
        # return super().get_queryset().filter(job=area)


#trabajo

class listarTrabajo(ListView):
    template_name = 'empleados/listByTrabajo.html'

    def get_queryset(self):
        trabajo = self.kwargs['job']
        print(trabajo)
        lista = Empleado.objects.filter(
            job = trabajo
        )
        return lista
    


#palabra clave
class ListarPalabraClave(ListView):
    template_name = 'empleados/listarPalabraClave.html'
    # context_object_name = 'empleados'

    def get_queryset(self):
        print("********")
        palabraClave = self.request.GET.get("keyword", " ")
        lista = Empleado.objects.filter(
            firstName = palabraClave
        )
        print('lista resultado: ', lista)

        return lista



class ListarHabilidades (ListView):
    template_name = 'empleados/listaHabilidades.html'
    context_object_name = 'habilidades'


    # la funcion get me retorna un unico registro de la base de datos 
    def get_queryset(self):
        identificador = self.kwargs['id']
        empleado = Empleado.objects.get(
            id = identificador
        )
        return empleado.habilidades.all()


class EmpleadoInfo (DetailView):
    model = Empleado
    template_name = 'empleados/empleadosInfo.html'

    #get context data para mandara variables de la vista a el template

    def get_context_data(self, **kwargs):
        context = super(EmpleadoInfo, self).get_context_data(**kwargs)
        #proceso
        context['titulo'] = 'empleado del mes'
        return context
    

class CrearEmpleado(CreateView):
    model = Empleado
    template_name = 'empleados/add.html'
    fields = ['firstName', 'lastName', 'job', 'departamento', 'habilidades', 'hojaVida', 'img']
    success_url = reverse_lazy('empleados_app:listaEmpladosAdmin')

    #esta funcion se ejecutara automaticamente cunado el proceso del formulario sea valido
    def form_valid(self, form):

        #logica del proceso

        #se esta almacenando tola la informacion que se ingreso en el formulario, de esta manera se trata la variable empleado
        #como on objeto de tipo empleado
        empleado = form.save(commit = False)
        empleado.nombreCompleto = empleado.firstName + ' ' + empleado.lastName
        empleado.save()
        print(empleado)


        return super(CrearEmpleado, self).form_valid(form)

class TemplateAdd (TemplateView):
    template_name = 'empleados/registrado.html'


class ActualizarEmpleado(UpdateView):
    model = Empleado
    template_name = 'empleados/actualizarEmpleados.html'
    fields = ['firstName', 'lastName', 'job', 'departamento', 'habilidades', 'hojaVida']
    success_url = reverse_lazy('empleados_app:listaEmpladosAdmin')


    # son dos metodos distintos el valid se llama cuando ya se verifica que los datos a guardar son validos, en cambi el 
    # post se llama antes de eso, 

    def post(self, request, *args, **kwargs):
        # en este caso "request" seria los valores que estemos guardando y podemos acceder a ellos com un diccionario 
        print(request.POST['firstName'])
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):

        return super(ActualizarEmpleado, self).form_valid(form)
    

class EliminarEmpleado (DeleteView):
    model = Empleado
    template_name = 'empleados/eliminarEmpleado.html'
    success_url = reverse_lazy('empleados_app:listaEmpladosAdmin')


class Inicio (TemplateView):
    template_name = 'inicio.html'
