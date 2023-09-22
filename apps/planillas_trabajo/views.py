from rest_framework                 import viewsets, status
from apps.feriados.models           import Feriado
from .models                        import PlanillaTrabajo
from .serializer                    import PlanillaTrabajoSerializer, HistorialPresentesSerializer
from apps.user_type.permisions      import IsAdministrador, IsSuper, IsSupervisor
from rest_framework.response        import Response
from apps.trabajadores.models       import Trabajador
from apps.trabajadores.serializer   import TrabajadorSerializer
from datetime                       import datetime, date

class PlanillaTrabajoViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar planillas de trabajo.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    las planillas de trabajo. Los usuarios con permisos de administrador o superusuario
    pueden acceder a esta vista.

    Parámetros de la solicitud:
    - fecha: Fecha de la planilla de trabajo en formato 'YYYY-MM-DD'.

    Ejemplo de solicitud JSON para crear una planilla de trabajo:
    {
        "id_plan_trabajo": 1,
        "id_trabajador": 1,
        "fecha": "2023-09-06",
        "horario_inicio": "09:00:00",
        "horario_fin": "17:00:00",
        "laborable": true,
        "presente": false
    }

    La vista verifica si la fecha proporcionada es un día no laborable consultando
    la base de datos de feriados. Si la fecha es un día no laborable, se devuelve un
    error.

    Permisos requeridos:
    - El usuario debe tener permisos de administrador o superusuario para acceder
      a esta vista.
    """
    queryset            = PlanillaTrabajo.objects.all()
    serializer_class    = PlanillaTrabajoSerializer
    permission_classes  = [IsAdministrador | IsSuper]

    def create(self, request, *args, **kwargs):
        try:
            fecha = request.data.get("fecha")
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            if Feriado.objects.filter(fecha=fecha):
                return Response({'error': "La fecha seleccionada es un dia no laborable"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Manejo de excepciones
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PresenteViewSet(viewsets.ViewSet):
    """
    Vista para marcar la asistencia de trabajadores en una planilla de trabajo.

    Esta vista permite marcar la asistencia de trabajadores en una planilla de
    trabajo identificada por su ID de planilla de trabajo. Se espera que se
    proporcione el ID de la planilla de trabajo en el cuerpo de la solicitud POST,
    así como una lista de identificadores de empleados a marcar como presentes o ausentes.

    Parámetros de la solicitud:
    - planilla_id: ID de la planilla de trabajo en la que se marcará la asistencia.
    - employes: Lista de identificadores de empleados a marcar como presentes o ausentes.

    Ejemplo de solicitud JSON:
    {
        "planilla_id": 1,
        "employes": [1, 2, 3]
    }

    La vista marca la asistencia de los empleados especificados y actualiza el estado de
    asistencia en la base de datos.

    Permisos requeridos:
    - El usuario debe tener permisos de administrador, superusuario o supervisor
      para acceder a esta vista.
    """
    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]

    def create(self, request):
        try:
            id = request.data.get('planilla_id')
            planilla_today = PlanillaTrabajo.objects.filter(id_plan_trabajo=id)
            if planilla_today:
                for planilla in planilla_today:
                    if (planilla.id_trabajador.id) in request.data.get("employes"):  # type: ignore
                        planilla.presente = not planilla.presente
                    planilla.save()
            return Response({"estado": "presentes aplicados"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
                planilla_today = PlanillaTrabajo.objects.filter(
                    id_plan_trabajo=id)
                if planilla_today:
                    trabajadores = []
                    for planilla in planilla_today:
                        trabajadores.append(Trabajador.objects.filter(
                            id=planilla.id_trabajador.id).first())   # type: ignore
                    serializer = TrabajadorSerializer(
                        trabajadores, many=True)
                    return Response(serializer.data)
                return Response([])
            return Response({"error": "no se reconoce el identificador"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PresentesEntreFechasPorIdTrabajador(viewsets.ViewSet):
    """
    Vista para obtener el historial de asistencia de un trabajador entre dos fechas.

    Esta vista permite obtener el historial de asistencia de un trabajador
    especificado por su ID entre dos fechas dadas. Se espera que se proporcione
    el ID del trabajador, la fecha de inicio y la fecha de fin en el cuerpo de
    la solicitud POST.

    Parámetros de la solicitud:
    - id_trabajador: ID del trabajador del cual se desea obtener el historial.
    - fecha_inicio: Fecha de inicio del período para el historial de asistencia.
    - fecha_fin: Fecha de fin del período para el historial de asistencia.

    Ejemplo de solicitud JSON:
    {
        "id_trabajador": 1,
        "fecha_inicio": "2023-01-01",
        "fecha_fin": "2023-12-31"
    }

    La vista realiza una consulta en la base de datos y devuelve el historial
    de asistencia en el formato deseado.

    Permisos requeridos:
    - El usuario debe tener permisos de administrador, superusuario o supervisor
      para acceder a esta vista.
    """
    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]

    def create(self, request, *args, **kwargs):
        try:
            id_trabajador = request.data.get('id_trabajador')
            fecha_inicio = request.data.get('fecha_inicio')
            fecha_fin = request.data.get('fecha_fin')

            # Verificar si fecha_inicio es menor que fecha_fin
            if fecha_inicio >= fecha_fin:
                return Response({"error": "La fecha de inicio debe ser anterior a la fecha de fin"}, status=status.HTTP_400_BAD_REQUEST)

            fecha_inicio = date.fromisoformat(fecha_inicio)
            fecha_fin = date.fromisoformat(fecha_fin)

            queryset = PlanillaTrabajo.objects.filter(
                id_trabajador=id_trabajador,
                fecha__range=(fecha_inicio, fecha_fin)
            )
            serializer = HistorialPresentesSerializer(queryset, many=True)

            return Response(serializer.data)
        except ValueError as e:
            print(e)
            return Response({"error": "Formato de fecha incorrecto"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": "Error en la consulta"}, status=status.HTTP_400_BAD_REQUEST)
