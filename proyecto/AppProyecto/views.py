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

def setGatos(request):
    if request.method == 'POST':
        miFormulario = formSetGatos(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            gato = Gato(nombre=data["nombre"],edad=data["edad"], color = data["color"])
            gato.save()
            return render(request, "AppProyecto/inicio.html")
    else:
        miFormulario = formSetGatos()
        return render(request, "AppProyecto/setGatos.html", {"miFormulario":miFormulario})

def getGatos(request):
    return render (request, "AppProyecto/getGatos.html")

def buscarGatos(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        gatos = Gato.objects.filter(nombre= nombre)
        return render(request, "AppProyecto/getGatos.html", {"gatos":gatos})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

def setCaballos(request):
    if request.method == 'POST':
        miFormulario = formSetCaballos(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            caballo = Caballo(nombre=data["nombre"],edad=data["edad"], peso = data["peso"],velocidad = data["velocidad"])
            caballo.save()
            return render(request, "AppProyecto/inicio.html")
    else:
        miFormulario = formSetCaballos()
        return render(request, "AppProyecto/setCaballos.html", {"miFormulario":miFormulario})

def getCaballos(request):
    return render (request, "AppProyecto/getCaballos.html")

def buscarCaballos(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        caballos = Caballo.objects.filter(nombre= nombre)
        return render(request, "AppProyecto/getCaballos.html", {"caballos":caballos})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

# Create your views here.

