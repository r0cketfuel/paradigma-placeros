
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Incident
from .serializer import IncidentSerializer
from .filter import IncidentFilter

# from rest_framework.response import Response
# from django.db.models import Count, Func


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]


class IncidentByMonthViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    filterset_class = IncidentFilter
