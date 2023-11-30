from rest_framework             import viewsets
from .models                    import Cuestionario
from .serializer                import CuestionarioSerializer
from apps.user_type.permissions import IsAdministrador, IsSuper, IsSupervisor


class CuestionarioViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar cuestionarios.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    los cuestionarios. Los usuarios con permisos de administrador, superusuario o supervisor
    pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase Cuestionario.

    """
    queryset            = Cuestionario.objects.all()
    serializer_class    = CuestionarioSerializer
    permission_classes  = [IsAdministrador | IsSuper | IsSupervisor]
