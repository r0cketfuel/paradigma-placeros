from rest_framework import viewsets
from .models import EspacioTrabajo
from .serializer import EspacioTrabajoSerializer
from rest_framework.permissions import IsAuthenticated


class EspacioTrabajoViewSet(viewsets.ModelViewSet):
    queryset = EspacioTrabajo.objects.all()
    serializer_class = EspacioTrabajoSerializer
    permission_classes = [IsAuthenticated]
