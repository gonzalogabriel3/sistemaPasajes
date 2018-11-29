from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import *
from .forms import *
import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from jinja2 import Environment, FileSystemLoader
# Create your views here

#################################INDEX'S#################################################

def generarPDF(request):
	#Indico el tipo de contenido
	response = HttpResponse(content_type='application/pdf')
	#Indico el nombre del archivo pdf generado
	response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

	buffer = BytesIO()
	p = canvas.Canvas(buffer)

#ESCRIBIENDO EN EL PDF
	#Seteo el estilo de la fuente
	p.setFont("Times-Roman",18)
	#Escribo el titulo en esas coordenadas(x,y)
	p.drawString(250, 800, 'Reporte')
	#Agrego una linea debajo del titulo
	p.line(50,750,560,750)



	
#FIN DE ESCRITURA EN EL PDF
	
	p.showPage()
	p.save()
	
	pdf = buffer.getvalue()
	buffer.close()
	
	response.write(pdf)

	return response


def generarPDF2(request):

	env=Environment(loader=FileSystemLoader("/"))
	template=env.get_template("indexAgente.html")

	html=template.render()
	print(html)

	return

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

#********ABM AGENTE***********#
def altaAgente(request):

	#Recibo el request,si es un request de tipo POST lo valido y guardo el nuevo agente
	if(request.method == 'POST'):
		
		form=formularioAgente(request.POST)	
		#Valido el formulario
		if(form.is_valid()):
				agente=form.save(commit=False)
				agente.save()
				return redirect('agente')
	
	#Si el request no es POST(GET) creo el formulario y lo renderizo en una vista
	else:
		form=formularioAgente()
		titulo="Agregar nuevo agente"
		
	return render(request,'formularios/agente.html',{'form':form,'titulo':titulo})

def bajaAgente(request,idAgente):

	agente=Agente.objects.get(id=idAgente)

	if(request.method=="POST"):
		agente.delete()
		return redirect('agente')

	texto="el agente '"+agente.nombre+" "+agente.apellido+"',con id "+str(agente.id)+"?"
	nombreUrl="agente"

	return render(request,'confirmaciones/eliminar.html',{'texto':texto,'nombreUrl':nombreUrl})

def modificacionAgente(request,idAgente):

	agente=Agente.objects.get(id=idAgente)
	#Si se ingresa por GET creo el formulario y paso como instancia los datos de un agente
	if(request.method == 'GET'):
		form=formularioAgente(instance=agente)
		titulo="Modificar agente"
	#Si por el contrario se ingresa por POST valido el formulario y guardo los datos en el agente	
	elif(request.method == "POST"):
		form=formularioAgente(request.POST, instance = agente)
		if(form.is_valid()):
			form.save()
			return redirect('agente')

	
	return render(request,'formularios/agente.html',{'form':form,'agente':agente,'titulo':titulo})

#********FIN ABM AGENTE***********#


#********ABM LOCALIDAD***********#
def altaLocalidad(request):

	#Recibo el request,si es un request de tipo POST lo valido y guardo el nuevo agente
	if(request.method == 'POST'):
		
		form=formularioLocalidad(request.POST)	
		#Valido el formulario
		if(form.is_valid()):
				localidad=form.save(commit=False)
				localidad.save()
				return redirect('localidad')
	
	#Si el request no es POST(GET) creo el formulario y lo renderizo en una vista
	else:
		form=formularioLocalidad()
		titulo="Agregar nueva localidad"
		
	return render(request,'formularios/localidad.html',{'form':form,'titulo':titulo})



def bajaLocalidad(request,idLocalidad):

	localidad=Localidad.objects.get(id=idLocalidad)

	if(request.method=="POST"):
		localidad.delete()
		return redirect('localidad')

	texto="la localidad '"+localidad.nombre+"',con id "+str(localidad.id)+"?"
	nombreUrl="localidad"

	return render(request,'confirmaciones/eliminar.html',{'texto':texto,'nombreUrl':nombreUrl})

def modificacionLocalidad(request,idLocalidad):

	localidad=Localidad.objects.get(id=idLocalidad)
	#Si se ingresa por GET creo el formulario y paso como instancia los datos de un Localidad
	if(request.method == 'GET'):
		form=formularioLocalidad(instance=localidad)
		titulo="Modificar localidad"
	#Si por el contrario se ingresa por POST valido el formulario y guardo los datos en el Localidad	
	elif(request.method == "POST"):
		form=formularioLocalidad(request.POST, instance = localidad)
		if(form.is_valid()):
			form.save()
			return redirect('localidad')

	
	return render(request,'formularios/localidad.html',{'form':form,'localidad':localidad,'titulo':titulo})


#********FIN ABM LOCALIDAD***********#


#********ABM FAMILIAR***********#
def altaFamiliar(request):

	if(request.method == 'POST'):
		
		form=formularioFamiliar(request.POST)	
		#Valido el formulario
		if(form.is_valid()):
				familiar=form.save(commit=False)
				familiar.save()
				return redirect('familiar')
	
	#Si el request no es POST(GET) creo el formulario y lo renderizo en una vista
	else:
		form=formularioFamiliar()
		titulo="Agregar nuevo familiar"
		
	return render(request,'formularios/familiar.html',{'form':form,'titulo':titulo})

def bajaFamiliar(request,idFamiliar):

	familiar=Familiar.objects.get(id=idFamiliar)

	if(request.method=="POST"):
		familiar.delete()
		return redirect('familiar')

	texto="el familiar '"+familiar.nombre+" "+familiar.apellido+"',con id "+str(familiar.id)+"?"
	nombreUrl="familiar"

	return render(request,'confirmaciones/eliminar.html',{'texto':texto,'nombreUrl':nombreUrl})

def modificacionFamiliar(request,idFamiliar):

	familiar=Familiar.objects.get(id=idFamiliar)
	#Si se ingresa por GET creo el formulario y paso como instancia los datos de un Familiar
	if(request.method == 'GET'):
		form=formularioFamiliar(instance=familiar)
		titulo="Modificar familiar"
	#Si por el contrario se ingresa por POST valido el formulario y guardo los datos en el Familiar	
	elif(request.method == "POST"):
		form=formularioFamiliar(request.POST, instance = familiar)
		if(form.is_valid()):
			form.save()
			return redirect('familiar')

	
	return render(request,'formularios/familiar.html',{'form':form,'familiar':familiar,'titulo':titulo})


#********FIN ABM FAMILIAR***********#



#********ABM EMPRESA***********#
def altaEmpresa(request):

	if(request.method == 'POST'):
		
		form=formularioEmpresa(request.POST)	
		#Valido el formulario
		if(form.is_valid()):
				empresa=form.save(commit=False)
				empresa.save()
				return redirect('empresa')
	
	#Si el request no es POST(GET) creo el formulario y lo renderizo en una vista
	else:
		form=formularioEmpresa()
		titulo="Agregar nueva empresa"
		
	return render(request,'formularios/empresa.html',{'form':form,'titulo':titulo})


def bajaEmpresa(request,idEmpresa):

	empresa=Empresa.objects.get(id=idEmpresa)

	if(request.method=="POST"):
		empresa.delete()
		return redirect('empresa')

	texto="la empresa '"+empresa.nombre+"',con id "+str(empresa.id)+"?"
	nombreUrl="empresa"

	return render(request,'confirmaciones/eliminar.html',{'texto':texto,'nombreUrl':nombreUrl})

def modificacionEmpresa(request,idEmpresa):

	empresa=Empresa.objects.get(id=idEmpresa)
	#Si se ingresa por GET creo el formulario y paso como instancia los datos de un Empresa
	if(request.method == 'GET'):
		form=formularioEmpresa(instance=empresa)
		titulo="Modificar empresa"
	#Si por el contrario se ingresa por POST valido el formulario y guardo los datos en el Empresa	
	elif(request.method == "POST"):
		form=formularioEmpresa(request.POST, instance = empresa)
		if(form.is_valid()):
			form.save()
			return redirect('empresa')

	
	return render(request,'formularios/empresa.html',{'form':form,'empresa':empresa,'titulo':titulo})


#********FIN ABM EMPRESA***********#


#********ABM PASAJE***********#
def altaPasaje(request):

	
	if(request.method == 'POST'):
		
		form=formularioPasaje(request.POST)	
		#Valido el formulario
		if(form.is_valid()):
				pasaje=form.save(commit=False)
				
				#(Si se desea que la fecha de emision sea automatica)pasaje.fecha_emision=datetime.datetime.now()
				pasaje.save()
				return redirect('pasaje')
	
	#Si el request no es POST(GET) creo el formulario y lo renderizo en una vista
	else:
		form=formularioPasaje()
		titulo="Agregar nuevo pasaje"
		
	return render(request,'formularios/pasaje.html',{'form':form,'titulo':titulo})

def bajaPasaje(request,idPasaje):

	pasaje=Pasaje.objects.get(id=idPasaje)

	if(request.method=="POST"):
		pasaje.delete()
		return redirect('pasaje')

	texto="el pasaje '"+str(pasaje.id)+"',emitido el dia "+str(pasaje.fecha_emision)+"?"
	nombreUrl="pasaje"

	return render(request,'confirmaciones/eliminar.html',{'texto':texto,'nombreUrl':nombreUrl})

def modificacionPasaje(request,idPasaje):

	pasaje=Pasaje.objects.get(id=idPasaje)
	#Si se ingresa por GET creo el formulario y paso como instancia los datos de un Pasaje
	if(request.method == 'GET'):
		form=formularioPasaje(instance=pasaje)
		titulo="Modificar Pasaje"
	#Si por el contrario se ingresa por POST valido el formulario y guardo los datos en el Pasaje	
	elif(request.method == "POST"):
		form=formularioPasaje(request.POST, instance = pasaje)
		if(form.is_valid()):
			form.save()
			return redirect('pasaje')

	
	return render(request,'formularios/pasaje.html',{'form':form,'pasaje':pasaje,'titulo':titulo})


#********FIN ABM PASAJE***********#


