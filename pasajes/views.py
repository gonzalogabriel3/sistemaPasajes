from django.shortcuts import render
from django.http import HttpResponse
from .models import Agente
# Create your views here

def index(request):
	return HttpResponse("Hola mundo!")

def agente(request,agente_id):
	return HttpResponse("Identificador de agente:  %s" %agente_id)

#Funcion para retornar los datos de la tabla de agente
def indexAgente(request):
	agentes=Agente.objects.all()
	output=""
	
	for agen in agentes:
		output+=str(agen.id)+":"+agen.nombre+" "+agen.apellido+"\n"
	
	return HttpResponse(output)

#Funcion para retornar los datos de la tabla de agente renderizados en un template
def indexAgente2(request):
	agentes=Agente.objects.all()
	
	context={
		'agentes':agentes,
	}
	
	return render(request, 'pasajes/templates/prueba.html', context)