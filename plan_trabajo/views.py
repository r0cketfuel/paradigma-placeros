from rest_framework import viewsets
from .models import PlanTrabajo
from .serializer import PlanTrabajoSerializer
from rest_framework.permissions import IsAuthenticated


class PlanTrabajoViewSet(viewsets.ModelViewSet):
    queryset = PlanTrabajo.objects.all()
    serializer_class = PlanTrabajoSerializer
    permission_classes = [IsAuthenticated]
