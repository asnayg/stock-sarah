# Register your models here.

from django.contrib import admin
from .models import Producto, OrdenSalida, OrdenEntrada, OrdenDevolucion

admin.site.index_title = "Sistema de Stock de TCC"
admin.site.site_header = "Stock System"
admin.site.site_title = "TCC Stock Admin Portal"

#Elimina la opcion de eliminar una entidad desde el admin.
admin.site.disable_action('delete_selected')


class OrdenEntradaInline(admin.StackedInline):
    model = OrdenEntrada


class ProductoAdmin(admin.ModelAdmin):
     fieldsets = [
         ('Datos del Producto',                 {'fields': ['identificador', 'marca', 'modelo', 'estado','ubicacion']}),
         ('Observaciones', {'fields': ['observacion'], 'classes': ['collapse']}),
     ]
     inlines = [OrdenEntradaInline]
     list_display = ('identificador', 'estado', 'cantidad', 'ubicacion' , 'fecha_actualizacion')
     list_per_page = 50
     readonly_fields = ["cantidad"]
     list_filter = ("estado", "ubicacion", "fecha_actualizacion",)
     list_display_links = None


class OrdenSalidaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'estado', 'cantidad_producto', 'producto' , 'fecha_creacion')
    list_per_page = 50
    list_filter = ("estado", "cantidad_producto", 'fecha_creacion')
    #actions = ['delete_selected']
    #actions = None


class OrdenDevolucionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cantidad_producto', 'orden_salida', 'fecha_creacion')
    list_per_page = 50
    list_filter = ("cantidad_producto", 'fecha_creacion')
    #actions = ['delete_selected']


admin.site.register(Producto, ProductoAdmin)
admin.site.register(OrdenSalida, OrdenSalidaAdmin)
admin.site.register(OrdenDevolucion, OrdenDevolucionAdmin)
#admin.site.register(OrdenEntrada)