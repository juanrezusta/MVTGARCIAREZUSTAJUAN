from django.db import models
import datetime

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camara=models.IntegerField()
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)
    
class Entregable(models.Model):
    nombre= models.CharField(max_length=40)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()