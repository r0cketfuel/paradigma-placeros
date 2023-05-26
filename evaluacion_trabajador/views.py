from rest_framework import viewsets
from .models import EvaluacionTrabajador
from .serializer import EvaluacionTrabajadorSerializer
from rest_framework.permissions import IsAuthenticated


class EvaluacionTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionTrabajador.objects.all()
    serializer_class = EvaluacionTrabajadorSerializer
    permission_classes = [IsAuthenticated]
