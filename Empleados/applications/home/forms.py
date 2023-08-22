from django import forms
from .models import prueba


class PruebaForm(forms.ModelForm):
    

    class Meta:
        model = prueba  
        fields = ('__all__')
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder' : 'ingrese un texto aqui',
                }
            )
        }
    
    # funcion que se usa vara obtener valores de los campos del formulario y hacer validaciones con dicho valor 
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 10:
            raise forms.ValidationError('ingrese un numero mayor a 10')
        
        return cantidad
    
    
