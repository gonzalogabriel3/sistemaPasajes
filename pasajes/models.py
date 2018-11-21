from django.db import models

# Create your models here.
class Localidad(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	nombre=models.CharField(max_length=200)

	def __str__(self):
		return str(self.id)+"/"+self.nombre

class Agente(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	id_localidad=models.ForeignKey(Localidad, on_delete=models.CASCADE)
	documento=models.IntegerField(unique=True)
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	fecha_nacimiento=models.DateField()

	def __str__(self):
		return str(self.id)+"/"+str(self.documento)+"/"+self.apellido+"-"+self.nombre+"/"+str(self.fecha_nacimiento)

class Familiar(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	documento=models.IntegerField(unique=True)
	id_agente=models.ForeignKey(Agente, on_delete=models.CASCADE)
	id_localidad=models.ForeignKey(Localidad, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	fecha_nacimiento=models.DateField()

	def __str__(self):
		return self.apellido+"/"+self.nombre

class Empresa(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	id_localidad=models.ForeignKey(Localidad, on_delete=models.CASCADE)
	cuit=models.IntegerField(unique=True)
	nombre=models.CharField(max_length=200)

	def __str__(self):
		return self.nombre+"/"+str(self.cuit)

class Pasaje(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	id_agente=models.ForeignKey(Agente, on_delete=models.CASCADE)
	id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
	fecha_emision=models.DateField()
	origen=models.CharField(max_length=200)
	destino=models.CharField(max_length=200)

	def __str__(self):
		return str(self.id)+"/"+self.origen+"-"+self.destino+"/"+self.id_empresa.nombre


