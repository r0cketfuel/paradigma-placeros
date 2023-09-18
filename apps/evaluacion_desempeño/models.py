from django.db                  import models
from apps.cuestionario.models   import Cuestionario
from apps.plan_trabajo.models   import PlanTrabajo

class EvaluacionDesempeño(models.Model):
    """
    Modelo para representar una evaluación de desempeño.

    Este modelo define los campos necesarios para representar una evaluación de desempeño,
    incluyendo su descripción, una referencia al cuestionario asociado, una referencia al
    plan de trabajo relacionado, una fecha y una ubicación.

    Campos del modelo:
    - description: Descripción de la evaluación de desempeño.
    - id_cuestionario: Referencia al cuestionario asociado.
    - id_plan_trabajo: Referencia al plan de trabajo relacionado.
    - fecha: Fecha de la evaluación de desempeño.
    - ubicación: Ubicación donde se realizó la evaluación.

    """
    description     = models.TextField()
    id_cuestionario = models.ForeignKey(Cuestionario,   on_delete=models.CASCADE, null=False, default=None)
    id_plan_trabajo = models.ForeignKey(PlanTrabajo,    on_delete=models.CASCADE, null=False, default=None)
    fecha           = models.DateField(null=False)
    ubicacion       = models.TextField()

    class Meta:
        db_table = 'evaluacion_desempeño'

    def __str__(self):
        return self.description
