from django.urls import path, include
from AppProyecto.views import  *

urlpatterns = [
    path('inicio/', inicio),
    path('caballos/', caballos, name="Caballos"),
    path('perros/', perros, name="Perros"),
    path('gatos/', gatos, name="Gatos"),
    path('setPerros/', setPerros, name="SetPerros"),
    path('getPerros/', getPerros, name="GetPerros"),
    path('buscarPerros/', buscarPerros, name="BuscarPerros")
]   