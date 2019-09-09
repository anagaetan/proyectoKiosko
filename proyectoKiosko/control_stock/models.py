from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Producto(models.Model):
    
    codigo= models.CharField(max_length=100, unique=True, null=False)
    nombre= models.CharField(max_length=100, null=False)
    descripcion= models.CharField(max_length=500, null=False)
    precio= models.DecimalField(max_digits=7, decimal_places=2, null=False, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre
