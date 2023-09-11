from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.empleados.models import Empleado
from .models import Departamento
from django.views.generic import ListView

# Create your views here.

class NewDepartamento(FormView):
    template_name = 'departamentos/crearDepartamento.html'
    form_class = NewDepartamentoForm
    success_url = '.'

    def form_valid(self, form):
        print('hola mundo')

        depa = form.cleaned_data['departamento']
        shortName = form.cleaned_data['shortName']
        dep = Departamento(
            name = depa,
            shortName = shortName
        )
        dep.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        Empleado.objects.create(
            firstName = nombre,
            lastName = apellido,
            job = '1',
            departamento = dep 
        )
        return super(NewDepartamento, self).form_valid(form)
    

 
 
class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamentos/listDepartamentos.html"
    context_object_name = 'departamentos'
