from rest_framework import viewsets
from .models import Cuestionario
from .serializer import CuestionarioSerializer
from user_type.permisions import IsAdministrador, IsSuper, IsSupervisor


class CuestionarioViewSet(viewsets.ModelViewSet):
    queryset = Cuestionario.objects.all()
    serializer_class = CuestionarioSerializer
    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]
