from django.db import models
from django.core.validators import MinLengthValidator




def validate_multiple_of_3(value):
    if value % 3 != 0:
        raise models.ValidationError(
            f'{value} is not a multiple of 3'
        )

# Create your models here.

class Cita(models.Model):
    ncliente = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    acliente = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    dni = models.CharField(max_length=9, validators=[MinLengthValidator(9)])
    fechaCita = models.DateField()
    horaCita = models.TimeField()
    medicacion = models.BooleanField(default=False)
    nombre_medicamento = models.CharField(blank=True, max_length=100)
    dosisDiaria = models.IntegerField(blank=True, validators=[validate_multiple_of_3])
    