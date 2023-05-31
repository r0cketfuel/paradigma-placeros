from rest_framework import viewsets
from .models import EvaluacionDesempeño
from .serializer import EvaluacionDesempeñoSerializer
from rest_framework.permissions import IsAuthenticated


class EvaluacionDesempeñoViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionDesempeño.objects.all()
    serializer_class = EvaluacionDesempeñoSerializer
    permission_classes = [IsAuthenticated]
