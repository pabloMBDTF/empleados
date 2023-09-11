from django.db import models
from applications.departamentos.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=70)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'

    def __str__ (self):
        return str(self.id) + ' - ' + self.habilidad    



#1899
class Empleado (models.Model):

    jobChoices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Programador(a)'),
        ('4', 'Otro'),
    )

    firstName = models.CharField('Nombres', max_length=50)
    lastName = models.CharField('Apellidos', max_length=50)
    nombreCompleto = models.CharField('nombre completo', max_length=120, blank = True)
    job = models.CharField('Trabajo', max_length=1, choices = jobChoices )
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE, default = None)
    habilidades = models.ManyToManyField(Habilidades) 
    hojaVida = RichTextField(blank = True, null = True)
    # avatar = models.ImageField(upload_to = 'empleado', blank = True, null = True)
    img = models.ImageField(upload_to='', blank = True, null = True)


    class Meta:
        verbose_name = 'Mis empleados'
        verbose_name_plural = 'Empleados'
        ordering = ['firstName']
        unique_together = ('firstName',)


    def __str__ (self):
        return str(self.id) + ' - ' + self.firstName + ' - ' + self.lastName

