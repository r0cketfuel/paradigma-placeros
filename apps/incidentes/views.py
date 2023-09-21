
from apps.user_type.permisions  import IsAdministrador, IsSuper, IsSupervisor
from rest_framework             import viewsets
from .models                    import Incident
from .serializer                import IncidentSerializer
from .filter                    import IncidentFilter


class IncidenteViewSet(viewsets.ModelViewSet):
    queryset            = Incident.objects.all()
    serializer_class    = IncidentSerializer
    permission_classes  = [IsAdministrador | IsSuper | IsSupervisor]


class IncidentByMonthViewSet(viewsets.ModelViewSet):
    queryset            = Incident.objects.all()
    serializer_class    = IncidentSerializer
    filterset_class     = IncidentFilter
    permission_classes  = [IsAdministrador | IsSuper | IsSupervisor]
