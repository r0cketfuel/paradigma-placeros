from django.utils               import timezone
from django.db                  import models
from apps.planes_trabajo.models import PlanTrabajo


class Incident(models.Model):
    STATE_INCIDENTS = [
        ('pendiente',   'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('finalizado',  'Finalizado'),
        ('informado',   'Informado'),
    ]

    descripcion     = models.TextField()
    estado          = models.CharField(max_length=20, choices=STATE_INCIDENTS, default='pendiente')
    plan_trabajo    = models.ForeignKey(PlanTrabajo, null=False, on_delete=models.RESTRICT)
    imagen          = models.ImageField(upload_to='incidente_images/', blank=True)
    fecha           = models.DateTimeField(default=timezone.now, editable=False)  # type: ignore
    activo          = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'incidentes'

    def __str__(self):
        return self.descripcion

    def delete(self):
        self.activo = False
        self.save()