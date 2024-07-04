from django.db import models
from Apps.login.models import Usuario 
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    tipoUnidad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precioUnitario = models.FloatField()
    importeTotal = models.FloatField()

class Inventario(models.Model):
    productos = models.ManyToManyField(Producto)

class Detalle(models.Model):
    tipo_movimiento = models.CharField(max_length=255)
    date = models.DateField()
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class HistorialMovimientos(models.Model):
    tipo_movimiento = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE) 

class Cliente(models.Model):
    nombre = models.CharField(max_length = 225)
    telefono = models.IntegerField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=100)

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fecha = models.DateField()
    importe_total = models.FloatField()
    detalles = models.ManyToManyField(Detalle)

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    fecha = models.DateField()
    importe_total = models.FloatField()
    detalles = models.ManyToManyField(Detalle)

class Reporte(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total = models.FloatField()

class ReporteVentas(Reporte):
    ventas = models.ManyToManyField(Venta)
    total_ventas = models.FloatField()


class ReporteCompras(Reporte):
    ventas = models.ManyToManyField(Compra)
    total_ventas = models.FloatField()

