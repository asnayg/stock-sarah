from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    update_date = models.DateTimeField('date update')

    def __str__(self):
        return self.nombre
