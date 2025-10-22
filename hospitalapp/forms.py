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
            'ncliente': {
                'max_length': 'El nombre es demasiado largo',
                'min_length': 'El nombre es demasiado corto, deberia de tener {limit_value} caracteres'
            },
            'acliente': {
                'max_length': 'Los apellidos son demasiado largos',
                'min_length': 'Los apellidos son demasiado cortos, deberia de tener {limit_value} caracteres'
            },
            'nombre_medicamento': {
                'max_length': 'El nombre del medicamento es demasiado largo',
                'min_length': 'El nombre del medicamento es demasiado corto, deberia de tener {limit_value} caracteres'
            },
            'dosisDiaria': {
                'invalid': 'La dosis diaria debe ser un numero entero',
            },
            'fechaCita': {
                'invalid': 'La fecha no es valida',
            },
            'horaCita': {
                'invalid': 'La hora no es valida',
            },
            'dni': {
                'max_length': 'El DNI es demasiado largo',
                'min_length': 'El DNI es demasiado corto, deberia de tener {limit_value} caracteres'
            }
        }