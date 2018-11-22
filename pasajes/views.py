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
def altaAgente(request):

	#Recibo el request,si es un request de tipo POST lo valido y guardo el nuevo agente
	if(request.method == 'POST'):
		
		form=formularioAgente(request.POST)	
		#Valido el formulario
		if(form.is_valid()):
				agente=form.save(commit=False)
				agente.save()
				return HttpResponseRedirect('agente')
	
	#Si el request no es POST(GET) creo el formulario y lo renderizo en una vista
	else:
		form=formularioAgente()
		
	return render(request,'formularios/agente.html',{'form':form})

def modificacionAgente(request,idAgente):
	
	agente=Agente.objects.get(id= idAgente)
	#Si se ingresa por GET creo el formulario y paso como instancia los datos de un agente
	if(request.method == 'GET'):
		form=formularioAgente(instance=agente)
	#Si por el contrario se ingresa por POST valido el formulario y guardo los datos en el agente	
	else:
		form=formularioAgente(request.POST,instance = agente)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect('agente')
	
	return render(request,'formularios/agente.html',{'form':form,'agente':agente})
