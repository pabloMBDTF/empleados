from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listarEmpleados/', views.ListAllEmpleados.as_view()),
    path('listarPorArea/', views.ListarPorArea.as_view()),

]
