from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MultipleofValidator

# Create your models here.

class Cita(models.Model):
    ncliente = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    acliente = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    dni = models.CharField(max_length=9, validators=[MinLengthValidator(9)])
    fechaCita = models.DateField()
    horaCita = models.TimeField()
    medicacion = models.BooleanField(default=False)
    nombre_medicamento = models.CharField(max_length=100)
    dosisDiaria = models.CharField(max_length=50, validators=[MinLengthValidator(2), MultipleofValidator(3)])
    