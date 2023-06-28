from django.db import models


class Trabajador(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
