from django.db                      import models
from apps.cooperativas.models       import Cooperativa
from apps.espacio_trabajo.models    import EspacioTrabajo
from apps.users.models              import CustomUser

class PlanTrabajo(models.Model):
    """
    Modelo para representar un plan de trabajo.

    Este modelo define los campos necesarios para representar un plan de trabajo, incluyendo
    su nombre, la cooperativa asociada, el espacio de trabajo asignado, el supervisor
    responsable, el tipo de servicio y la fecha de creación.

    Campos del modelo:
    - name: Nombre del plan de trabajo.
    - id_cooperativa: Referencia a la cooperativa asociada.
    - id_espacio: Referencia al espacio de trabajo asignado.
    - id_supervisor: Referencia al supervisor responsable.
    - tipo_servicio: Tipo de servicio del plan de trabajo.
    - fecha_creacion: Fecha de creación del plan de trabajo.

    """
    name            = models.TextField()
    id_cooperativa  = models.ForeignKey(Cooperativa,    null=False, on_delete=models.CASCADE)
    id_espacio      = models.ForeignKey(EspacioTrabajo, null=False, on_delete=models.CASCADE)
    id_supervisor   = models.ForeignKey(CustomUser,     null=False, on_delete=models.CASCADE)
    tipo_servicio   = models.TextField()
    fecha_creacion  = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'planes_trabajo'

    def __str__(self):
        return self.name
