from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)

    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)