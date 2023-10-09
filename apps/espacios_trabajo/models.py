from django.db import models


class EspacioTrabajo(models.Model):

    nombre      = models.TextField(max_length=50)
    image       = models.ImageField(upload_to='espacio_trabajo_images/', blank=True)
    address     = models.CharField(blank=True, max_length=30)
    activo      = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'espacios_trabajo'

    def __str__(self):
        return self.nombre

    def delete(self):
        self.activo = False
        self.save()