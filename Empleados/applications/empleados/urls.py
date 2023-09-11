from django.contrib import admin
from django.urls import path
from . import views

app_name = "empleados_app"


urlpatterns = [
    path('listarEmpleados/', views.ListAllEmpleados.as_view(), name="listarEmpleados"),
    path('empleadosAdmin/', views.ListaEmpleadosAdmin.as_view(), name="listaEmpladosAdmin"),
    path('listarPorArea/<shortName>', views.ListarPorArea.as_view(), name="ListarArea"),
    path('listarPorTrabajo/<job>', views.listarTrabajo.as_view()),
    path('listarPorKw/', views.ListarPalabraClave.as_view()),
    path('listarHabilidades/<id>', views.ListarHabilidades.as_view()),
    path('empleadosInfo/<pk>', views.EmpleadoInfo.as_view(), name="empleadosInfo"),
    path('addempleado/', views.CrearEmpleado.as_view(), name = "crearEmp"),
    path('succes/', views.TemplateAdd.as_view(), name = 'correcto'),
    path('actualizarEmpleado/<pk>', views.ActualizarEmpleado.as_view(), name = 'actualizar'),
    path('eliminarEmpleado/<pk>', views.EliminarEmpleado.as_view(), name = 'eliminar'),
    path('', views.Inicio.as_view(), name = 'inicio'),



]
