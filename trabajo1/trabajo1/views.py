
from AppCoder.models import *
from django.template import loader
from django.http import HttpResponse

def familia(self):
    diccionario={"padre":padre,"madre":madre,"hijo":hijo}
    plantilla=loader.get_template("plantillabase.html")
    documento=plantilla.render(diccionario)
    
    return HttpResponse(documento)