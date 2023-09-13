from rest_framework import viewsets
from .models import PlanTrabajo
from .serializer import PlanTrabajoSerializer
from apps.user_type.permisions import IsAdministrador, IsSuper


class PlanTrabajoViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar planes de trabajo.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    los planes de trabajo. Los usuarios con permisos de administrador o superusuario
    pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase PlanTrabajo.

    """
    queryset = PlanTrabajo.objects.all()
    serializer_class = PlanTrabajoSerializer
    permission_classes = [IsAdministrador | IsSuper]
