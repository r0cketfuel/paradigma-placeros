from rest_framework import viewsets
from .models import Cuestionario
from .serializer import CuestionarioSerializer
from rest_framework.permissions import IsAuthenticated


class CuestionarioViewSet(viewsets.ModelViewSet):
    queryset = Cuestionario.objects.all()
    serializer_class = CuestionarioSerializer
    permission_classes = [IsAuthenticated]
