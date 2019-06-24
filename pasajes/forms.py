from django import forms
from .models import *
from django_select2.forms import *

class formularioAgente(forms.ModelForm):

	id_localidad=forms.ModelChoiceField(label="Localidad",queryset=Localidad.objects.all(),widget=Select2Widget)
	
	#Creo los campos con el mismo nombre que el modelo para poder darle estilos
	nombre = forms.CharField(max_length=100,label="Nombre del agente",
		widget = forms.TextInput(attrs = {'class': 'form-control','placeholder':'Nombre del nuevo agente'} ))

	apellido = forms.CharField(max_length=100,label="Apellido del agente",
		widget = forms.TextInput(attrs = {'class': 'form-control','placeholder':'Apellido del nuevo agente'} ))

	documento = forms.IntegerField(label="Documento del agente",
		widget = forms.NumberInput(attrs = {'class': 'form-control','placeholder':'N° de documento del nuevo agente'} ))

	fecha_nacimiento=forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class':'datepicker',
                                    'placeholder':'Fecha de nacimiento'

                                }))
	#id_localidad=forms.IntegerField(label="Localidad",widget=forms.Select(queryset=Localidad.objects.all()))

	class Meta:
		model=Agente
		exclude=['id']


class formularioLocalidad(forms.ModelForm):
	
	#Creo los campos con el mismo nombre que el modelo para poder darle estilos
	nombre = forms.CharField(max_length=100,label="Nombre de la localidad",
		widget = forms.TextInput(attrs = {'class': 'form-control','placeholder':'Nombre de la nueva localidad'}))

	class Meta:
		model=Localidad
		exclude=['id']


class formularioFamiliar(forms.ModelForm):
	
	id_localidad=forms.ModelChoiceField(label="Localidad",queryset=Localidad.objects.all(),widget=Select2Widget)

	id_agente=forms.ModelChoiceField(label="Familiar del agente",queryset=Agente.objects.all(),widget=Select2Widget)

	#Creo los campos con el mismo nombre que el modelo para poder darle estilos
	nombre = forms.CharField(max_length=100,label="Nombre del familiar",
		widget = forms.TextInput(attrs = {'class': 'form-control','placeholder':'Nombre del nuevo familiar'} ))

	apellido = forms.CharField(max_length=100,label="Apellido del familiar",
		widget = forms.TextInput(attrs = {'class': 'form-control','placeholder':'Nombre del nuevo familiar'} ))

	documento = forms.IntegerField(label="Documento del familiar",
		widget = forms.NumberInput(attrs = {'class': 'form-control','placeholder':'N° de documento del nuevo familiar'} ))

	fecha_nacimiento=forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class':'datepicker',
                                    'placeholder':'Fecha de nacimiento'
                                }))

	
	class Meta:
		model=Familiar
		exclude=['id']


class formularioEmpresa(forms.ModelForm):
	
	id_localidad=forms.ModelChoiceField(label="Localidad",queryset=Localidad.objects.all(),widget=Select2Widget)

	#Creo los campos con el mismo nombre que el modelo para poder darle estilos
	nombre = forms.CharField(max_length=100,label="Nombre de la empresa",
		widget = forms.TextInput(attrs = {'class': 'form-control','placeholder':'Nombre de la nueva empresa'} ))

	cuit = forms.IntegerField(label="Cuit",
		widget = forms.NumberInput(attrs = {'class': 'form-control','placeholder':'N° de Cuit de la nueva empresa'} ))

	class Meta:
		model=Empresa
		exclude=['id']

class formularioPasaje(forms.ModelForm):
	VIAS = (
		('Terrestre', 'Terrestre'),
	    ('Aerea', 'Aerea')
	)

	id_empresa=forms.ModelChoiceField(label="Empresa",queryset=Empresa.objects.all(),widget=Select2Widget(attrs={'name':'id_empresa'}))

	via=forms.ChoiceField(label="Via",choices=VIAS,widget=Select2Widget(attrs={'name':'via'}))

	fecha_viaje=forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class':'datepickerPasaje',
                                    'name':'fecha_viaje',
                                    'placeholder':'Fecha de viaje'
                                }))
	
	#Creo los campos con el mismo nombre que el modelo para poder darle estilos
	origen = forms.CharField(max_length=100,label="Origen",
		widget = forms.TextInput(attrs = {'class': 'form-control','name':'origen','placeholder':'Ingrese origen del viaje'} ))

	destino =  forms.CharField(max_length=100,label="Destino",
		widget = forms.TextInput(attrs = {'class': 'form-control','name':'destino','placeholder':'Ingrese destino del viaje'} ))

	class Meta:
		model=Pasaje
		exclude=['id','fecha_emision','id_agente','id_familiar'] 
