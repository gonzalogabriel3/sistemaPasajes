from django import forms
from .models import *

class formularioAgente(forms.ModelForm):
	
	#Creo los campos con el mismo nombre que el modelo para poder darle estilos
	nombre = forms.CharField(max_length=100,label="Nombre del agente",
		widget = forms.TextInput(attrs = {'class': 'form-control'} ))

	apellido = forms.CharField(max_length=100,label="Apellido del agente",
		widget = forms.TextInput(attrs = {'class': 'form-control'} ))

	documento = forms.IntegerField(label="Documento del agente",
		widget = forms.NumberInput(attrs = {'class': 'form-control'} ))

	fecha_nacimiento=forms.DateField(label="Fecha nacimiento",
		widget = forms.DateInput(attrs = {'class' : 'form-control'}))

	#id_localidad=forms.IntegerField(label="Localidad",widget=forms.Select(queryset=Localidad.objects.all()))

	class Meta:
		model=Agente
		exclude=['id']

	
        