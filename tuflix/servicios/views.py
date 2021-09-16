from django.shortcuts import render
 


#para imprimir mensajes sencillos de respuesta 
from django.http import HttpResponse
from servicios.models import *
from datetime import datetime

def vistaEjemplo(request):
    """
    contiene toda la informacion de usuario que hace
    la peticion a traves de metodos GET y POST

    GET -- metodo con el cual el usuario solicita acceder a una URL
    POST -- metodo con el cual el usuario envia la información a una URL 
    """
    #hoy = datetime.now()
    Shakira = Musico.objects.get(nombre="Shakira")
    #(nombre="Fonseca", apellido="Perez", salario=500000)
    return HttpResponse("Hola, estás en la aplicación Servicios, con el musico "+Shakira.nombre)
    

# Create your views here.
