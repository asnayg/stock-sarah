from django.db import models
import datetime

# Create your models here.

class Producto(models.Model):
    ESTADOS = (
        ('S', 'Stock'),
        ('B', 'BackUp'),
        ('U', 'En USO'),
    )
    identificador = models.CharField(max_length=200, unique=True )
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, choices=ESTADOS)
    ubicacion = models.CharField(max_length=200, default="Deposito")
    observacion = models.TextField(blank=True)
    fecha_actualizacion = models.DateField(editable=False, default=datetime.date.today)
    cantidad = models.PositiveIntegerField(editable=False, default=0)

    def __str__(self):
        return self.identificador

    def actualizarCantidad(self, cant):
        self.cantidad += cant
        super().save()

    class Meta:
        ordering = ["fecha_actualizacion"]
        verbose_name_plural = "Productos"


class Orden(models.Model):
    numero = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateField()
    cantidad_producto = models.PositiveIntegerField(default=0)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return self.observacion

    class Meta:
        abstract = True


class OrdenEntrada(Orden):
    producto = models.OneToOneField(Producto, on_delete=models.PROTECT)
    proveedor = models.CharField(max_length=200)

    def __str__(self):
        return "Orden Entrada"

    def  updateCantidadProducto(self):
        self.producto.actualizarCantidad(self.cantidad_producto)

    def save(self, *args, **kwargs):
        self.updateCantidadProducto()
        super().save(*args, **kwargs)

    class Meta:
       verbose_name_plural = "Ordenes de Entrada"


class OrdenSalida(Orden):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    ORDEN_ESTADOS = (
        ('A', 'Activa'),
        ('C', 'Cerrada'),
        ('M', 'Modificada'),
    )
    estado = models.CharField(max_length=1, choices=ORDEN_ESTADOS)

    def __str__(self):
        return self.numero

    def  updateCantidadProducto(self):
        self.producto.actualizarCantidad((self.cantidad_producto * -1))

    def save(self, *args, **kwargs):
        self.updateCantidadProducto()
        super().save(*args, **kwargs)

    class Meta:
       verbose_name_plural = "Ordenes de Salida"


class OrdenDevolucion(Orden):
    orden_salida = models.ForeignKey(OrdenSalida, verbose_name="Orden de Salida", on_delete=models.PROTECT) #.SET_DEFAULT

    def __str__(self):
        return self.numero

    def  updateCantidadProducto(self):
        self.orden_salida.producto.actualizarCantidad(self.cantidad_producto)

    def save(self, *args, **kwargs):
        self.updateCantidadProducto()
        super().save(*args, **kwargs)

    class Meta:
       verbose_name_plural = "Ordenes de Devolucion"
