from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here

#################################INDEX'S#################################################

def index(request):
	return render(request, 'index.html')


#Funcion para retornar los datos de la tabla de agente renderizados en un template
def indexAgenteView(request):
	agentes=Agente.objects.all().order_by('-id')
	
	context={
		'agentes':agentes,
	}
	
	return render(request, 'indexAgente.html', context)

def indexLocalidadView(request):
	localidades=Localidad.objects.all().order_by('-id')
	
	context={
		'localidades':localidades,
	}
	
	return render(request, 'indexLocalidad.html', context)

def indexFamiliarView(request):
	familiares=Familiar.objects.all().order_by('-id')
	
	context={
		'familiares':familiares,
	}
	
	return render(request, 'indexFamiliar.html', context)

def indexEmpresaView(request):
	empresas=Empresa.objects.all().order_by('-id')
	
	context={
		'empresas':empresas,
	}
	
	return render(request, 'indexEmpresa.html', context)

def indexPasajeView(request):
	pasajes=Pasaje.objects.all().order_by('-id')
	
	context={
		'pasajes':pasajes,
	}
	
	return render(request, 'indexPasaje.html', context)


################FIN DE INDEX'S########################################


################FORMULARIOS###########################################
def abmAgente(request,idAgente):

	#Recibo el request
	if(request.method == 'POST'):
		#Si no se recibio ningun id de un agente,valido el formulario y guardo un nuevo agente
		if(idAgente==0):

			form=formularioAgente(request.POST)
			
			
		#Si se recibe un id creo un formulario en base a los datos del agente
		else:
			agente=Agente.objects.get(pk=idAgente)
			form=formularioAgente(instance=agente)
			
		#Valido el formulario
		if(form.is_valid()):
				agente=form.save(commit=False)
				agente.save()
				return HttpResponseRedirect('agente')

	else:
		form=formularioAgente()
		
	return render(request,'formularios/agente.html',{'form':form})