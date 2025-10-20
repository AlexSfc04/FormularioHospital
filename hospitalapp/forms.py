from django import forms
from hospitalapp.models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        labels = {
            'ncliente': 'Nombre del cliente'
        }
        widgets = {
            'fechaCita': forms.DateInput(attrs={'type':'date'})
        }
        error_messages = {
            'dni': {
                'max_length': 'El DNI es demasiado largo',
                'min_length': 'El DNI es demasiado corto, deberia de tener {limit_value} caracteres'
            }
        }