from django import forms

class formSetPerros(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    raza = forms.CharField(max_length=30)

class formSetGatos(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    color = forms.CharField(max_length=30)

class formSetCaballos(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    peso = forms.IntegerField()
    velocidad = forms.IntegerField()