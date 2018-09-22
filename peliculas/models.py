from django.db import models


class Actor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    foto = models.ImageField(upload_to='fotos-de-actores', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Director(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Pelicula(models.Model):
    nombre = models.CharField(max_length=60)
    fecha_de_estreno = models.DateField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)

    actores = models.ManyToManyField(Actor, blank=True) 

    def __str__(self):
        return '{} {}'.format(self.nombre, self.fecha_de_estreno)