from django.db import models

class prueba (models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)