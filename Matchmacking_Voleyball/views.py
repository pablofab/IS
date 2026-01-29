from django.http import HttpResponse
from django.template.loader import get_template

def saludo(request): #Primera vista
    return HttpResponse("Hola mundo")


def home(self):
    plantilla = get_template("index2.html")
    return HttpResponse(plantilla.render())



