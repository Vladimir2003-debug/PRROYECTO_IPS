from django.contrib import admin
from .models import (Producto,
                    Inventario,
                    Detalle,
                    HistorialMovimientos,
                    Cliente,
                    Venta,
                    Compra,
                    Reporte,
                    ReporteVentas,
                    Proveedor,
                    ReporteCompras,
                    )
# Register your models here.

admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(HistorialMovimientos)
admin.site.register(Cliente)
admin.site.register(Inventario)
admin.site.register(Venta)
admin.site.register(Compra)
admin.site.register(Proveedor)
admin.site.register(ReporteCompras)
admin.site.register(ReporteVentas)


