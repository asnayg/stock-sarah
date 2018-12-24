from django.db import models
import datetime

# Create your models here.

class Producto(models.Model):
    CATEGORIAS = (
        ('A', 'Redes'),
        ('B', 'TV'),
        ('C', 'Insumo'),
    )
    identificador = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    observacion = models.TextField(blank=True)
    fecha_entrada = models.DateField(editable=False, default=datetime.date.today)
    cantidad = models.PositiveIntegerField(editable=False, default=0)
    categoria = models.CharField(max_length=1, choices=CATEGORIAS, default='S')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.identificador

    def actualizarCantidad(self, cant):
        self.cantidad += cant
        super().save()

    class Meta:
        ordering = ["fecha_entrada"]
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

    def updateCantidadProducto(self):
        self.producto.actualizarCantidad(self.cantidad_producto)

    def save(self, *args, **kwargs):
        self.updateCantidadProducto()
        super().save(*args, **kwargs)

    class Meta:
       verbose_name_plural = "Ordenes de Entrada"


class Cliente(models.Model):
    ubicacion = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.ubicacion

    class Meta:
       verbose_name_plural = "Clientes Destinos"


class OrdenSalida(Orden):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cliente_destino = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return self.numero

    def updateCantidadProducto(self):
        self.producto.actualizarCantidad((self.cantidad_producto * -1))

    def save(self, *args, **kwargs):
        self.updateCantidadProducto()
        super().save(*args, **kwargs)

    class Meta:
       verbose_name_plural = "Ordenes de Salida"


class OrdenDevolucion(Orden):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cliente_destino = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return self.numero

    def updateCantidadProducto(self):
        self.producto.actualizarCantidad(self.cantidad_producto)

    def save(self, *args, **kwargs):
        self.updateCantidadProducto()
        super().save(*args, **kwargs)

    class Meta:
       verbose_name_plural = "Ordenes de Devolucion"


class StockCliente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cliente_destino = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(editable=False, default=0)

    def __str__(self):
        return "Stock Cliente"

    class Meta:
       verbose_name_plural = "Stock en Clientes"
