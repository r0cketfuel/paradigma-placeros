from rest_framework import viewsets
from .models import Incident
from .serializer import IncidentSerializer
from rest_framework.permissions import IsAuthenticated


class IncidenteViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]
