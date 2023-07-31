from django.db import models


class Feriado(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()

    def __str__(self):
        return self.descripcion
