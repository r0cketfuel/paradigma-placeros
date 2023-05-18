from rest_framework import viewsets
from .models import Cooperativa
from .serializer import CooperativaSerializer
from rest_framework.permissions import IsAuthenticated


class CooperativaViewSet(viewsets.ModelViewSet):
    queryset = Cooperativa.objects.all()
    serializer_class = CooperativaSerializer
    permission_classes = [IsAuthenticated]
