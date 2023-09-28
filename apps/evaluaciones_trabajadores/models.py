from django.db                  import models
from apps.trabajadores.models   import Trabajador
from apps.users.models          import CustomUser


class EvaluacionTrabajador(models.Model):
    """
    Modelo para representar una evaluación de trabajador.

    Este modelo define los campos necesarios para representar una evaluación de trabajador,
    incluyendo el trabajador evaluado, el coordinador que realiza la evaluación, el resultado
    de la evaluación y el tipo de evaluación (por ejemplo, uniforme, EPP, herramientas).

    Campos del modelo:
    - trabajador: Referencia al trabajador evaluado.
    - coordinador: Referencia al coordinador que realiza la evaluación.
    - resultado_evaluacion: Resultado de la evaluación (opciones: bueno, regular, malo).
    - tipo_evaluacion: Tipo de evaluación (opciones: uniforme, EPP, herramientas).

    """
    EVALUATION_RESULT = [
        ('bueno',   'Bueno'),
        ('regular', 'Regular'),
        ('malo',    'Malo'),
    ]
    
    EVALUATION_TYPE = [
        ('uniforme',        'Uniforme'),
        ('epp',             'EPP'),
        ('herramientas',    'Herramientas'),
    ]

    trabajador              = models.ForeignKey(Trabajador, null=False, on_delete=models.RESTRICT)
    coordinador             = models.ForeignKey(CustomUser, null=False, on_delete=models.RESTRICT)
    resultado_evaluacion    = models.CharField(max_length=20, choices=EVALUATION_RESULT, default='Malo', null=False)
    tipo_evaluacion         = models.CharField(max_length=20, choices=EVALUATION_TYPE, default='Uniforme', null=False)

    class Meta:
        db_table = 'evaluaciones_trabajadores'

    def __str__(self):
        return f"{self.trabajador}  {self.coordinador}"
