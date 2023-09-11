from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"


urlpatterns = [
    path('nueboDepartamento/', views.NewDepartamento.as_view(), name = 'nueboDepartamento' ),
    path('listarDepartamento/', views.DepartamentoListView.as_view(), name = 'departamentoList' ),
]