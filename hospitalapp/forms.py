from django import forms
from hospitalapp.models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        labels = {
            'ncliente': 'Nombre del cliente',
            'acliente': 'Apellidos del cliente',
            'dni': 'DNI del cliente',
            'fechaCita': 'Fecha de la cita',
            'horaCita': 'Hora de la cita',
            'medicacion': '¿Toma medicacion?',
            'nombre_medicamento': 'Nombre del medicamento',
            'dosisDiaria': 'Dosis diaria',
        }
        widgets = {
            'fechaCita': forms.DateInput(attrs={'type':'date'}),
            'horaCita': forms.TimeInput(attrs={'type':'time'})
        }
        error_messages = {
            'dni': {
                'max_length': 'El DNI es demasiado largo',
                'min_length': 'El DNI es demasiado corto, deberia de tener {limit_value} caracteres'
            }
        }