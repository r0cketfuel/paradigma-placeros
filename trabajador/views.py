from rest_framework.response import Response
from rest_framework import viewsets
from .models import Trabajador
from .serializer import TrabajadorSerializer
from rest_framework.permissions import IsAuthenticated


class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]


class TrabajadoresCargadosViewSet(viewsets.ViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        trabajadores = Trabajador.objects.all()
        cargados = len(trabajadores) if trabajadores else 0
        return Response({"trabajadores_cargados": cargados}, status=200)


# TODO ESTADISTICAS
