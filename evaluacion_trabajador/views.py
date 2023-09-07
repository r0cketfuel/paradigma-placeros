from rest_framework import viewsets
from .models import EvaluacionTrabajador
from .serializer import EvaluacionTrabajadorSerializer
from user_type.permisions import IsAdministrador, IsSuper, IsCoordinador


class EvaluacionTrabajadorViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar evaluaciones de trabajadores.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    las evaluaciones de trabajadores. Los usuarios con permisos de administrador, superusuario
    o coordinador pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase EvaluacionTrabajador.

    """
    queryset = EvaluacionTrabajador.objects.all()
    serializer_class = EvaluacionTrabajadorSerializer
    permission_classes = [IsAdministrador | IsSuper | IsCoordinador]
