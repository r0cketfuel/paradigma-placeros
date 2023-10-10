from django.db                      import models
from apps.cooperativas.models       import Cooperativa
from apps.espacios_trabajo.models   import EspacioTrabajo
from apps.users.models              import CustomUser


class PlanTrabajo(models.Model):

    nombre          = models.TextField()
    tipo_servicio   = models.TextField()
    cooperativa     = models.ForeignKey(Cooperativa, null=False, on_delete=models.RESTRICT)
    espacio         = models.ForeignKey(EspacioTrabajo, null=False, on_delete=models.RESTRICT)
    supervisor      = models.ForeignKey(CustomUser, null=False, on_delete=models.RESTRICT)
    fecha_creacion  = models.DateField(auto_now_add=True, null=True)
    activo          = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'planes_trabajo'

    def __str__(self):
        return self.nombre
    
    def delete(self):
        self.activo = False
        self.save()
