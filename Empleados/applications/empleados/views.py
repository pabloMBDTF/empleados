from django.shortcuts import render
from django.views.generic import (
    ListView
)

from .models import Empleado

# 1. listar todos los empleados de la empresa 
# 2. lisrtar empleados por area 
# 3. listar por trabajo 
# 4. lisrtar por palabra clave 
# 5. lisrtar por habilidades


class ListAllEmpleados(ListView):
    template_name = 'empleados/empleadosLista.html'
    model = Empleado
    context_object_name = 'lista'


class ListarPorArea(ListView):
    template_name = 'empleados/listByArea.html'
    queryset = Empleado.objects.filter(
        departamento__shortName = 'contabilidad'
    )