from django.db import models


class Cooperativa(models.Model):
    """
    Modelo para representar una cooperativa.

    Este modelo define los campos necesarios para representar una cooperativa, incluyendo su
    descripción.

    Campos del modelo:
    - description: Descripción de la cooperativa.

    """
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.description

