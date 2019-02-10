# Register your models here.

from django.contrib import admin
from .models import Producto, OrdenSalida, OrdenEntrada, OrdenDevolucion, Cliente, StockCliente

admin.site.index_title = "Sistema de Stock de TCC"
admin.site.site_header = "Stock System"
admin.site.site_title = "TCC Stock Admin Portal"

# Elimina la opcion de eliminar una entidad desde el admin.
admin.site.disable_action('delete_selected')

class OrdenEntradaInline(admin.StackedInline):
    model = OrdenEntrada


class ProductoAdmin(admin.ModelAdmin):
     fieldsets = [
         ('Datos del Producto', {'fields': ['nombre', 'identificador', 'marca', 'modelo', 'categoria', 'precio_unitario']}),
         ('Observaciones', {'fields': ['observacion'], 'classes': ['collapse']}),
     ]
     inlines = [OrdenEntradaInline]
     list_display = ('nombre', 'identificador', 'marca', 'modelo', 'cantidad', 'fecha_entrada', 'categoria', 'precio_unitario')
     list_per_page = 50
     readonly_fields = ["cantidad"]
     list_filter = ("fecha_entrada", 'categoria', 'nombre', 'marca')
     list_display_links = None


class OrdenSalidaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cantidad_producto', 'producto', 'fecha_creacion', 'cliente_destino')
    list_per_page = 50
    list_filter = ("cantidad_producto", 'fecha_creacion', 'cliente_destino', 'producto__identificador', 'producto__nombre')
    # actions = ['delete_selected']
    # actions = None


class OrdenDevolucionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cantidad_producto', 'producto', 'fecha_creacion', 'cliente_origen')
    list_per_page = 50
    list_filter = ("cantidad_producto", 'fecha_creacion', 'cliente_origen__ubicacion', 'producto__identificador', 'producto__nombre')
    # actions = ['delete_selected']
    # actions = None


class OrdenEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cantidad_producto', 'fecha_creacion', 'proveedor', 'producto')
    list_per_page = 50
    list_filter = ("cantidad_producto", 'fecha_creacion', 'proveedor', 'producto__identificador', 'producto__nombre')
    # actions = ['delete_selected']
    # actions = None


class StockClienteAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cliente_destino', 'cantidad')
    list_per_page = 50
    list_filter = ("cliente_destino__ubicacion", 'producto__identificador', 'producto__nombre')
    # actions = None


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('ubicacion', 'descripcion')
    list_per_page = 50
    # actions = None


admin.site.register(Producto, ProductoAdmin)
admin.site.register(OrdenSalida, OrdenSalidaAdmin)
admin.site.register(OrdenDevolucion, OrdenDevolucionAdmin)
admin.site.register(OrdenEntrada, OrdenEntradaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(StockCliente, StockClienteAdmin)

