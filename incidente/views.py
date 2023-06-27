from rest_framework import viewsets
from .models import Incident
from .serializer import IncidentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(images=self.request.FILES.getlist('images'))
