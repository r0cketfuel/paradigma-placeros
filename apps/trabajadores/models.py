from django.db import models


class Trabajador(models.Model):
    """
    Modelo para representar a un trabajador.

    Este modelo define los campos necesarios para representar a un trabajador, incluyendo su
    nombre, apellido y número de documento de identidad (DNI).

    Campos del modelo:
    - name: Nombre del trabajador.
    - last_name: Apellido del trabajador.
    - dni: Número de documento de identidad único del trabajador.

    """
    name        = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    dni         = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.id}"  # type: ignore
