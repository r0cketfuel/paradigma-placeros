from rest_framework.response import Response
from rest_framework import viewsets
from .models import Cooperativa
from .serializer import CooperativaSerializer
from apps.user_type.permisions import IsAdministrador, IsSuper
from apps.planilla_trabajo.models import PlanillaTrabajo


class CooperativaViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar cooperativas.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    las cooperativas. Los usuarios con permisos de administrador o superusuario pueden
    acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase Cooperativa.

    """
    queryset = Cooperativa.objects.all()
    serializer_class = CooperativaSerializer
    permission_classes = [IsAdministrador | IsSuper]


class EmpleadosPorCooperativa(viewsets.ViewSet):
    """
    Vista para obtener el total de trabajadores por cooperativa.

    Esta vista permite obtener el número total de trabajadores por cooperativa. Los usuarios
    pueden acceder a esta vista sin restricciones de permisos.

    La vista realiza una consulta en la base de datos para contar los trabajadores por cada
    cooperativa y devuelve el resultado.

    """

    def list(self, request):
        try:
            planillas = PlanillaTrabajo.objects.all()
            total_trabajadores_por_cooperativa = {}
            for planilla in planillas:
                cooperativa = planilla.id_plan_trabajo.id_cooperativa
                if cooperativa.description in total_trabajadores_por_cooperativa:
                    total_trabajadores_por_cooperativa[cooperativa.description] += 1
                else:
                    total_trabajadores_por_cooperativa[cooperativa.description] = 1
            return Response(total_trabajadores_por_cooperativa, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
