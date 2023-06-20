from django.db import models


class EspacioTrabajo(models.Model):
    description = models.TextField(max_length=50)
    image = models.ImageField(
        upload_to='espacio_trabajo_images/', null=True, blank=True)
    address = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.description
