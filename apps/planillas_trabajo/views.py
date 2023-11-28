from rest_framework                 import viewsets, status
from rest_framework.response        import Response
from .models                        import PlanillaTrabajo
from apps.trabajadores.models       import Trabajador
from .serializer                    import PlanillaTrabajoSerializer
from apps.trabajadores.serializer   import TrabajadorSerializer
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

class TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet(viewsets.ViewSet):
    """
    Vista para obtener la lista de trabajadores en una planilla de trabajo por ID de plan de trabajo.

    Esta vista permite obtener la lista de trabajadores que están asignados a una planilla de
    trabajo específica identificada por su ID de plan de trabajo. Se espera que se proporcione
    el ID de plan de trabajo en el cuerpo de la solicitud POST.

    Parámetros de la solicitud:
    - plan_trabajo_id: ID del plan de trabajo para el cual se desea obtener la lista de trabajadores.

    Ejemplo de solicitud JSON:
    {
        "plan_trabajo_id": 1
    }

    La vista realiza una consulta en la base de datos y devuelve la lista de trabajadores
    asignados a la planilla de trabajo especificada.

    Permisos requeridos:
    - El usuario debe tener permisos de administrador, superusuario o supervisor
      para acceder a esta vista.
    """

    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]

    def create(self, request):
        try:
            if request.data.get("plan_trabajo_id", None):
                id = request.data.get('plan_trabajo_id')
                planilla_today = PlanillaTrabajo.objects.filter(plan_trabajo_id=id)
                if planilla_today:
                    trabajadores = []
                    for planilla in planilla_today:
                        trabajador = Trabajador.objects.filter(id=planilla.trabajador_id).first()
                        if trabajador:
                            # Obtener los objetos PlanillaTrabajo asociados a Trabajador
                            planillas_trabajo = PlanillaTrabajo.objects.filter(trabajador_id=trabajador.id)
                            
                            # Serializar los objetos PlanillaTrabajo
                            serializer = PlanillaTrabajoSerializer(planillas_trabajo, many=True)
                            
                            # Agregar los resultados a la lista de trabajadores
                            trabajadores.extend(serializer.data)
                    
                    return Response(trabajadores)
                return Response([])
            return Response({"error": "no se reconoce el identificador"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
