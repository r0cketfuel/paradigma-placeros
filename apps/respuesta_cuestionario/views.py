from rest_framework import viewsets
from .models import RespuestaCuestionario
from .serializer import RespuestaCuestionarioSerializer
from apps.user_type.permisions import IsAdministrador, IsSuper, IsSupervisor


class RespuestaCuestionarioViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar respuestas a cuestionarios.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    las respuestas a cuestionarios. Los usuarios con permisos de administrador, superusuario
    o supervisor pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase RespuestaCuestionario.

    """
    queryset = RespuestaCuestionario.objects.all()
    serializer_class = RespuestaCuestionarioSerializer
    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]
