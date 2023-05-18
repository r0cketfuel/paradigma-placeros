from django.db import models


class EspacioTrabajo(models.Model):
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.description
# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
