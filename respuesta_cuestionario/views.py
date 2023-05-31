from rest_framework import viewsets
from .models import RespuestaCuestionario
from .serializer import RespuestaCuestionarioSerializer
from rest_framework.permissions import IsAuthenticated


class RespuestaCuestionarioViewSet(viewsets.ModelViewSet):
    queryset = RespuestaCuestionario.objects.all()
    serializer_class = RespuestaCuestionarioSerializer
    permission_classes = [IsAuthenticated]
