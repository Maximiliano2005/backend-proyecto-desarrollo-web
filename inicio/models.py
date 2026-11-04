from django.db import models

# Create your models here.

class Estacionamiento(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    ubicacion = models.CharField(max_length=10)
    disponible = models.BooleanField(default=True)
    precio_hora = models.DecimalField(max_digits=10, decimal_places=0)
    

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    

class Reserva(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=25,default="pendiente",choices=[
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada")
    ])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.PROTECT)
