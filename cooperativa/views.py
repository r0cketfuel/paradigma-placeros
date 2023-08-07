from rest_framework.response import Response
from rest_framework import viewsets
from .models import Cooperativa
from .serializer import CooperativaSerializer
from user_type.permisions import IsAdministrador, IsSuper
from planilla_trabajo.models import PlanillaTrabajo


class CooperativaViewSet(viewsets.ModelViewSet):
    queryset = Cooperativa.objects.all()
    serializer_class = CooperativaSerializer
    permission_classes = [IsAdministrador | IsSuper]


class EmpleadosPorCooperativa(viewsets.ViewSet):

    def list(self, request):
        try:
            planillas = PlanillaTrabajo.objects.all()
            total_trabajadores_por_cooperativa = {}
            for planilla in planillas:
                cooperativa = planilla.id_plan_trabajo.id_cooperativa
                print(cooperativa)
                if cooperativa.description in total_trabajadores_por_cooperativa:
                    total_trabajadores_por_cooperativa[cooperativa.description] += 1
                else:
                    total_trabajadores_por_cooperativa[cooperativa.description] = 1
            return Response(total_trabajadores_por_cooperativa, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
