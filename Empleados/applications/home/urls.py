from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.lista.as_view()),
    path('lista-prueba/', views.ModeloLista.as_view()),
    path('add/', views.add.as_view()),

]
