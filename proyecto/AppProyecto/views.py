from django.shortcuts import render
from AppProyecto.forms import *
from AppProyecto.models import *
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppProyecto/inicio.html")

def caballos(request):
    return render(request, "AppProyecto/caballos.html")

def perros(request):
    return render(request, "AppProyecto/perros.html")

def gatos(request):
    return render(request, "AppProyecto/gatos.html")

def setPerros(request):
    if request.method == 'POST':
        miFormulario = formSetPerros(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            perro = Perro(nombre=data["nombre"],edad=data["edad"], raza = data["raza"])
            perro.save()
            return render(request, "AppProyecto/inicio.html")
    else:
        miFormulario = formSetPerros()
        return render(request, "AppProyecto/setPerros.html", {"miFormulario":miFormulario})

def getPerros(request):
    return render (request, "AppProyecto/getPerros.html")

def buscarPerros(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        perros = Perro.objects.filter(nombre= nombre)
        return render(request, "AppProyecto/getPerros.html", {"perros":perros})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)



# Create your views here.

