from django.db                      import models
from apps.cooperativas.models       import Cooperativa
from apps.espacios_trabajo.models   import EspacioTrabajo
from apps.users.models              import CustomUser


class PlanTrabajo(models.Model):
    """
    Modelo para representar un plan de trabajo.

    Este modelo define los campos necesarios para representar un plan de trabajo, incluyendo
    su nombre, la cooperativa asociada, el espacio de trabajo asignado, el supervisor
    responsable, el tipo de servicio y la fecha de creación.

    Campos del modelo:
    - name: Nombre del plan de trabajo.
    - cooperativa: Referencia a la cooperativa asociada.
    - espacio: Referencia al espacio de trabajo asignado.
    - supervisor: Referencia al supervisor responsable.
    - tipo_servicio: Tipo de servicio del plan de trabajo.
    - fecha_creacion: Fecha de creación del plan de trabajo.

    """
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
