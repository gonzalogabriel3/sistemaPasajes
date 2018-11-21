from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here

#################################INDEX'S#################################################

def index(request):
	return render(request, 'index.html')


#Funcion para retornar los datos de la tabla de agente renderizados en un template
def indexAgenteView(request):
	agentes=Agente.objects.all()
	
	context={
		'agentes':agentes,
	}
	
	return render(request, 'indexAgente.html', context)

def indexLocalidadView(request):
	localidades=Localidad.objects.all()
	
	context={
		'localidades':localidades,
	}
	
	return render(request, 'indexLocalidad.html', context)

def indexFamiliarView(request):
	familiares=Familiar.objects.all()
	
	context={
		'familiares':familiares,
	}
	
	return render(request, 'indexFamiliar.html', context)

def indexEmpresaView(request):
	empresas=Empresa.objects.all()
	
	context={
		'empresas':empresas,
	}
	
	return render(request, 'indexEmpresa.html', context)

def indexPasajeView(request):
	pasajes=Pasaje.objects.all()
	
	context={
		'pasajes':pasajes,
	}
	
	return render(request, 'indexPasaje.html', context)


################FIN DE INDEX'S########################################


################FORMULARIOS###########################################
def abmAgente(request):
	form=formularioAgente()

	return render(request,'formularios/agente.html',{'form':form})