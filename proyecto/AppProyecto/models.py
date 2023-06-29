from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    raza = models.CharField(max_length=30)

class Gato(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    color = models.CharField(max_length=30)

class Caballo(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    peso = models.IntegerField()
    velocidad = models.IntegerField()

# Create your models here.
