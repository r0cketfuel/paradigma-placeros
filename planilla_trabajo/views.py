from rest_framework import viewsets, status
from .models import PlanillaTrabajo
from .serializer import PlanillaTrabajoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from trabajador.models import Trabajador
from trabajador.serializer import TrabajadorSerializer


class PlanillaTrabajoViewSet(viewsets.ModelViewSet):
    queryset = PlanillaTrabajo.objects.all()
    serializer_class = PlanillaTrabajoSerializer
    permission_classes = [IsAuthenticated]


class PresenteViewSet(viewsets.ViewSet):

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

    def create(self, request):
        try:
            if request.data.get("planilla_id", None):
                id = request.data.get('planilla_id')
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
