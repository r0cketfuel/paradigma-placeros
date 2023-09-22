from rest_framework.response        import Response
from rest_framework                 import viewsets
from .models                        import Cooperativa
from .serializer                    import CooperativaSerializer
from apps.user_type.permisions      import IsAdministrador, IsSuper
from apps.trabajadores.models       import Trabajador


class CooperativaViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar cooperativas.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    las cooperativas. Los usuarios con permisos de administrador o superusuario pueden
    acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase Cooperativa.

    """
    queryset            = Cooperativa.objects.all()
    serializer_class    = CooperativaSerializer
    permission_classes  = [IsAdministrador | IsSuper]


class TrabajadoresPorCooperativa(viewsets.ViewSet):
    """
    Vista para obtener el total de trabajadores por cooperativa.

    Esta vista permite obtener el número total de trabajadores por cooperativa. Los usuarios
    pueden acceder a esta vista sin restricciones de permisos.

    La vista realiza una consulta en la base de datos para contar los trabajadores por cada
    cooperativa y devuelve el resultado.

    """

    def list(self, request):
        cooperativas = Cooperativa.objects.all()
        data = []

        for cooperativa in cooperativas:
            trabajadores_count = Trabajador.objects.filter(id_cooperativa=cooperativa).filter(activo=True).count()
            data.append({
                'cooperativa_id':       cooperativa.id,
                'cooperativa_nombre':   cooperativa.nombre,
                'trabajadores_count':   trabajadores_count
            })

        return Response(data)
