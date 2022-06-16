import sqlite3
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from entregable_app.models import Familiares



def mtv(request):  
	return HttpResponse("MTV_ENTREGABLE FAMILIARES")


def familia(self, nombre, anios, parentesco, cumpleanios):

      anios = int(anios)

      familia = Familiares(nombre= nombre, anios= anios , parentesco= parentesco, cumpleanios= cumpleanios)
    
      familia.save()
      
      documento = f"<br><br>Hola mi nombre es: {familia.nombre}. <br> Soy {familia.parentesco} de Seba.<br> Cumplo el: {familia.cumpleanios}. <br> Tengo {familia.anios} años "

      return HttpResponse(documento)


def Templat(self):

    miHtml = open("C:/Users/cheba/Desktop/MTV_SWIDZINSKI_Seba/plantillas/template.html")
        
    plantilla = Template(miHtml.read()) 

    miHtml.close()
    
    miContexto = Context()

    documento = plantilla.render(miContexto) 

    return HttpResponse(documento)

def mostrar_familia(self):
      
      conn = sqlite3.connect("db.sqlite3")
      cursor = conn.cursor()
      rows = cursor.execute("SELECT nombre, anios, parentesco, cumpleanios FROM entregable_app_familiares").fetchall()
      

      return HttpResponse(rows)

