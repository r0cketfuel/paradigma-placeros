from rest_framework import viewsets
from .models import Incident
from .serializer import IncidentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Func


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]


class ExtractMonth(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'


class IncidentByMonthViewSet(viewsets.ModelViewSet):
    """
        list all incidents on the current month
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def incidents_by_month(self, request):
        # Obtener los incidentes agrupados por meses y contar la cantidad en cada mes
        incidentes_por_mes = Incident.objects.annotate(
            month=ExtractMonth('created_at')).values('month').annotate(count=Count('id'))
        # Devolver los datos en la respuesta
        return Response(incidentes_por_mes)
