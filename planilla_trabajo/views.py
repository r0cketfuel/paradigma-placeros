from rest_framework import viewsets, status
from .models import PlanillaTrabajo
from .serializer import PlanillaTrabajoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from trabajador.models import Trabajador
from trabajador.serializer import TrabajadorSerializer
import requests


class PlanillaTrabajoViewSet(viewsets.ModelViewSet):
    queryset = PlanillaTrabajo.objects.all()
    serializer_class = PlanillaTrabajoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:

            # ************************************************************
            # TODO: need to increase performance with cache
            # all this must be a function
            from datetime import datetime

            fecha = request.data.get("fecha")
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            response = requests.get(
                'http://nolaborables.com.ar/api/v2/feriados/2023?formato=mensual')
            if response.status_code == 200:
                response = response.json()
                if str(fecha.day) in response[int(fecha.month) - 1].keys():
                    return Response({'error': f"La fecha seleccionada es un dia no laborable: {fecha.day}-{fecha.month}:{response[int(fecha.month) - 1].get(str(fecha.day)).get('motivo')}"}, status=status.HTTP_400_BAD_REQUEST)

            # ************************************************************

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Manejo de excepciones
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
    '''
        Obtiene todos los trabajadores asignados a un plan de trabajo
        usando la siguiente sintaxis

        json con el campo

        "plan_trabajo_id":numero

    '''

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
