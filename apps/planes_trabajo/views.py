from rest_framework             import viewsets
from .models                    import PlanTrabajo
from .serializer                import PlanTrabajoSerializer
from apps.user_type.permissions import IsAdministrador, IsSuper
from django.db.models           import F


class PlanTrabajoViewSet(viewsets.ModelViewSet):

    queryset = PlanTrabajo.objects.select_related('cooperativa', 'espacio', 'supervisor').annotate(
        cooperativa_name    = F('cooperativa__nombre'),
        espacio_nombre      = F('espacio__nombre'),
        supervisor_nombre   = F('supervisor__username')
    )
    
    serializer_class        = PlanTrabajoSerializer
    permission_classes      = [IsAdministrador | IsSuper]