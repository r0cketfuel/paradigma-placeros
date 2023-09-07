from django.db import models


class EspacioTrabajo(models.Model):
    """
    Modelo para representar un espacio de trabajo.

    Este modelo define los campos necesarios para representar un espacio de trabajo, incluyendo
    su descripción, una imagen asociada y una dirección.

    Campos del modelo:
    - description: Descripción del espacio de trabajo.
    - image: Imagen asociada al espacio de trabajo (opcional).
    - address: Dirección del espacio de trabajo (opcional).

    """
    description = models.TextField(max_length=50)
    image = models.ImageField(
        upload_to='espacio_trabajo_images/', null=True, blank=True)
    address = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.description
