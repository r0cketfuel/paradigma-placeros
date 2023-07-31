# views.py

from rest_framework import viewsets
from .models import Feriado
from .serializers import FeriadoSerializer
from rest_framework.permissions import IsAuthenticated


class FeriadoViewSet(viewsets.ModelViewSet):
    queryset = Feriado.objects.all()
    serializer_class = FeriadoSerializer
    permission_classes = [IsAuthenticated]
