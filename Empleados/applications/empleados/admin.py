from django.contrib import admin
from .models import Empleado, Habilidades


admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'firstName',
        'lastName',
        'departamento',
        'job',
    )

    # Buscador en el administrador

    search_fields = ('firstName',)

    # filtrar en el administrador 

    list_filter = ('job', 'habilidades', 'departamento',) 

    # filtrar en el administrador, relaciones muchos a muchos

    filter_horizontal = ('habilidades',)



admin.site.register(Empleado, EmpleadoAdmin)
