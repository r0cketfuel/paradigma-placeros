from rest_framework import viewsets
from rest_framework.response import Response
from .models import EspacioTrabajo
from .serializer import EspacioTrabajoSerializer
from user_type.permisions import IsAdministrador, IsSuper, IsSupervisor
from planilla_trabajo.models import PlanillaTrabajo
from datetime import datetime


class EspacioTrabajoViewSet(viewsets.ModelViewSet):
    queryset = EspacioTrabajo.objects.all()
    serializer_class = EspacioTrabajoSerializer
    permission_classes = [IsAdministrador | IsSuper]


class PresentesPorEspacioDeTrabajo(viewsets.ViewSet):
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
