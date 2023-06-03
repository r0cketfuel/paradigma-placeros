from django.db import models


class EspacioTrabajo(models.Model):
    description = models.TextField(max_length=50)
    image = models.ImageField(
        upload_to='espacio_trabajo_images/', null=True, blank=True)

    def __str__(self):
        return self.description
