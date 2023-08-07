# views.py

from rest_framework import viewsets
from .models import Feriado
from .serializers import FeriadoSerializer
from user_type.permisions import IsAdministrador, IsSuper


class FeriadoViewSet(viewsets.ModelViewSet):
    queryset = Feriado.objects.all()
    serializer_class = FeriadoSerializer
    permission_classes = [IsAdministrador | IsSuper]
