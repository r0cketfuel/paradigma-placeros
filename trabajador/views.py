from rest_framework import viewsets
from .models import Trabajador
from .serializer import TrabajadorSerializer
from rest_framework.permissions import IsAuthenticated


class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]
