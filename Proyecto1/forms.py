
from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    carrera = forms.EmailField(label='Carrera')

class EstudianteForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    email = forms.EmailField(label='Email')
    apellido = forms.CharField(label='Apellido', widget=forms.Textarea)

class ProfesorForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)
    carrera = forms.EmailField(label='Carrera')