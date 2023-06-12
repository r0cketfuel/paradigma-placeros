from rest_framework import viewsets
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
        print(request.data)
        id = request.data.get('planilla_id')
        planilla_today = PlanillaTrabajo.objects.filter(id_plan_trabajo=id)
        if planilla_today:
            for planilla in planilla_today:
                print(planilla, planilla.presente, planilla.id_trabajador.id)
                if (planilla.id_trabajador.id) in request.data.get("employes"):
                    planilla.presente = not planilla.presente
                planilla.save()
        return Response("ok")


class TrabajadoresInPLanillaTrabajoByIdPlanTrabajoViewSet(viewsets.ViewSet):

    def create(self, request):

        if not isinstance(request.data, int):
            id = request.data.get('planilla_id')
        else:
            id = request.data
        print(id)
        planilla_today = PlanillaTrabajo.objects.filter(id_plan_trabajo=id)
        if planilla_today:
            trabajadores = []
            for planilla in planilla_today:
                trabajadores.append(Trabajador.objects.filter(
                    id=planilla.id_trabajador.id).first())

            serializer = TrabajadorSerializer(trabajadores, many=True)
            return Response(serializer.data)

        return Response([])
