from rest_framework import viewsets
from .models import PlanillaTrabajo
from .serializer import PlanillaTrabajoSerializer
from rest_framework.permissions import IsAuthenticated


class PlanillaTrabajoViewSet(viewsets.ModelViewSet):
    queryset = PlanillaTrabajo.objects.all()
    serializer_class = PlanillaTrabajoSerializer
    permission_classes = [IsAuthenticated]
