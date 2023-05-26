from django.db import models


class Trabajador(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
