import random
from django.db import models


class Trabajador(models.Model):
    name = models.TextField(default="")
    last_name = models.TextField(default="")
    dni = models.IntegerField()

    def __str__(self):
        return self.name
