from django.forms import ModelForm
from django import forms
from .models import *

class formularioAgente(ModelForm):
	nombre=forms.CharField(label='Nombre', max_length=100)
	apellido=forms.CharField(label='Apellido', max_length=100)
	documento=forms.IntegerField(label='Nro documento')
	localidad=forms.IntegerField(label='Localidad')
	fecha_nacimiento=forms.DateField(label='Fecha de nacimiento')

	class Meta:
		model=Agente
		fields="__all__"