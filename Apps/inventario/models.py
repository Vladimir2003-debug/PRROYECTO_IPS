from django.db import models
from Apps.login.models import Usuario 
# Create your models here.

class Producto(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    tipoUnidad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precioUnitario = models.FloatField()
    importeTotal = models.FloatField()

class Inventario(models.Model):
    id = models.IntegerField()
    productos = models.ManyToManyField(Producto)

class Detalle(models.Model):
    id = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=255)
    date = models.DateField()
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class HistorialMovimientos(models.Model):
    id = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(Usuario) 


