from rest_framework                 import viewsets, status
from .models                        import PlanillaTrabajo
from .serializer                    import PlanillaTrabajoSerializer
from apps.user_type.permisions      import IsAdministrador, IsSuper, IsSupervisor


class PlanillaTrabajoViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar planillas de trabajo.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    las planillas de trabajo. Los usuarios con permisos de administrador o superusuario
    pueden acceder a esta vista.
    """
    queryset            = PlanillaTrabajo.objects.all()
    serializer_class    = PlanillaTrabajoSerializer
    permission_classes  = [IsAdministrador | IsSuper]
