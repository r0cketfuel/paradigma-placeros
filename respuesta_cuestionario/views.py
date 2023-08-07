from rest_framework import viewsets
from .models import RespuestaCuestionario
from .serializer import RespuestaCuestionarioSerializer
from user_type.permisions import IsAdministrador, IsSuper, IsSupervisor


class RespuestaCuestionarioViewSet(viewsets.ModelViewSet):
    queryset = RespuestaCuestionario.objects.all()
    serializer_class = RespuestaCuestionarioSerializer
    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]
