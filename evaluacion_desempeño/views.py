from rest_framework import viewsets
from .models import EvaluacionDesempeño
from .serializer import EvaluacionDesempeñoSerializer
from rest_framework.permissions import IsAuthenticated


class EvaluacionDesempeñoViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar evaluaciones de desempeño.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    las evaluaciones de desempeño. Los usuarios autenticados pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase EvaluacionDesempeño.

    """
    queryset = EvaluacionDesempeño.objects.all()
    serializer_class = EvaluacionDesempeñoSerializer
    permission_classes = [IsAuthenticated]
