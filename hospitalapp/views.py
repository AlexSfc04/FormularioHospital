from django.http import HttpResponse
from django.shortcuts import render
from hospitalapp.forms import CitaForm

# Create your views here.

def form(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if  form.is_valid():
            form.save()
            return HttpResponse('Cita reservada')
    else:
        form = CitaForm()
    return render(request, 'hospitalapp/form.html', {'form' : form})