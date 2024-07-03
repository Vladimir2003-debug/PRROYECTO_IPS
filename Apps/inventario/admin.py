from django.contrib import admin
from .models import Producto,Inventario,Detalle,HistorialMovimientos,Cliente,Venta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(HistorialMovimientos)
admin.site.register(Cliente)
admin.site.register(Venta)

