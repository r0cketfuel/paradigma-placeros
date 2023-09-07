from rest_framework import viewsets
from rest_framework.response import Response
from .models import EspacioTrabajo
from .serializer import EspacioTrabajoSerializer
from user_type.permisions import IsAdministrador, IsSuper, IsSupervisor
from planilla_trabajo.models import PlanillaTrabajo
from datetime import datetime


class EspacioTrabajoViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar espacios de trabajo.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    los espacios de trabajo. Los usuarios con permisos de administrador o superusuario
    pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase EspacioTrabajo.

    """
    queryset = EspacioTrabajo.objects.all()
    serializer_class = EspacioTrabajoSerializer
    permission_classes = [IsAdministrador | IsSuper]


class PresentesPorEspacioDeTrabajo(viewsets.ViewSet):
    """
    Vista para obtener el total de trabajadores presentes en espacios de trabajo hoy.

    Esta vista permite obtener el número total de trabajadores presentes en los espacios de
    trabajo hoy. Los usuarios con permisos de administrador, superusuario o supervisor pueden
    acceder a esta vista.

    La vista realiza una consulta en la base de datos para contar los trabajadores presentes
    en cada espacio de trabajo y devuelve el resultado.

    """
    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]

    def list(self, request):
        try:
            hoy = datetime.today()
            hoy = datetime.strptime(
                f"{datetime.today().day}-{datetime.today().month}-{datetime.today().year}", "%d-%m-%Y")
            planillas = PlanillaTrabajo.objects.filter(
                fecha=hoy, presente=True)
            total_presentes_por_espacio_trabajo_today = {}
            for planilla in planillas:
                espacio = planilla.id_plan_trabajo.id_espacio
                if espacio.description in total_presentes_por_espacio_trabajo_today:
                    total_presentes_por_espacio_trabajo_today[espacio.description] += 1
                else:
                    total_presentes_por_espacio_trabajo_today[espacio.description] = 1

            return Response(total_presentes_por_espacio_trabajo_today, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

