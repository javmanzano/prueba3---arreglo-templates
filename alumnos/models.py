# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Cuenta(models.Model): #
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.email



class SolicitudContacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='')  # Default, es predeterminado si no falla por pk o fk
    email = models.EmailField()
    celular = models.IntegerField(blank=True)
    comentario = models.TextField(default='Sin comentario') # Default, es predeterminado si no falla por pk o fk
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"
    

class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes_platillos/')

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.platillo.nombre}"