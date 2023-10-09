
from apps.user_type.permisions  import IsAdministrador, IsSuper, IsSupervisor
from rest_framework             import viewsets
from .models                    import Incidente
from .serializer                import IncidenteSerializer
from .filter                    import IncidenteFilter


class IncidenteViewSet(viewsets.ModelViewSet):
    queryset            = Incidente.objects.all()
    serializer_class    = IncidenteSerializer
    permission_classes  = [IsAdministrador | IsSuper | IsSupervisor]


class IncidentByMonthViewSet(viewsets.ModelViewSet):
    queryset            = Incidente.objects.all()
    serializer_class    = IncidenteSerializer
    filterset_class     = IncidenteFilter
    permission_classes  = [IsAdministrador | IsSuper | IsSupervisor]
