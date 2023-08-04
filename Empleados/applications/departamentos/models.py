from django.db import models

# Create your models here.


class Departamento (models.Model):
    name = models.CharField('Nombre', max_length = 50, blank = True, unique = True)
    shortName = models.CharField('Nombre corto', max_length = 20 )
    active = models.BooleanField('Anulado', default = False)
    
    class Meta:
        verbose_name = 'mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'shortName')

    def __str__ (self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.shortName
