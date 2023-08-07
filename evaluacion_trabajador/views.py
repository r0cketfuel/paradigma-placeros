from rest_framework import viewsets
from .models import EvaluacionTrabajador
from .serializer import EvaluacionTrabajadorSerializer
from user_type.permisions import IsAdministrador, IsSuper, IsCoordinador


class EvaluacionTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionTrabajador.objects.all()
    serializer_class = EvaluacionTrabajadorSerializer
    permission_classes = [IsAdministrador | IsSuper | IsCoordinador]
