from django.db import models
from clientes.models import Cliente
from peliculas.models import Pelicula


class Alquiler(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    momento = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)


class AlquilerPelicula(models.Model):
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
