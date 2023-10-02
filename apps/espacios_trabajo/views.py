from rest_framework                     import generics
from apps.trabajadores.models           import Trabajador
from .models                            import EspacioTrabajo
from .serializer                        import EspacioTrabajoSerializer
from apps.user_type.permisions          import IsAdministrador, IsSuper, IsSupervisor
from apps.planillas_trabajo.models      import PlanillaTrabajo
from apps.trabajadores.serializer       import TrabajadorSerializer
from rest_framework.response            import Response
from apps.planes_trabajo.models         import PlanTrabajo
from rest_framework                     import status
from django.utils                       import timezone
from apps.feriados.models               import Feriado
from apps.dias_no_laborables.models     import DiaNoLaborable


class EspacioTrabajoListView(generics.ListCreateAPIView):

    queryset            = EspacioTrabajo.objects.all()
    serializer_class    = EspacioTrabajoSerializer
    permission_classes  = [IsAdministrador | IsSuper]


class EspacioTrabajoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset            = EspacioTrabajo.objects.all()
    serializer_class    = EspacioTrabajoSerializer
    permission_classes  = [IsAdministrador | IsSuper]


class TrabajadoresAsignadosListView(generics.ListAPIView):

    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]

    def list(self, request, espacio_trabajo_id=None):

        # Obtiene la fecha y hora actual en la zona horaria del servidor
        current_datetime = timezone.now()

        # Verificar si la fecha actual está en el modelo DiaNoLaborable
        dia_no_laborable = DiaNoLaborable.objects.filter(fecha=current_datetime.date()).first()
        if dia_no_laborable:
            return Response({"mensaje": f"Hoy es un día no laborable: {dia_no_laborable.descripcion}"}, status=status.HTTP_200_OK)

        # Verificar si la fecha actual está en el modelo Feriado
        feriado = Feriado.objects.filter(fecha=current_datetime.date()).first()
        if feriado:
            return Response({"mensaje": f"Hoy es un feriado: {feriado.descripcion}"}, status=status.HTTP_200_OK)

        # Obtiene el número de día de la semana actual (1 para lunes, 2 para martes, etc.)
        day_of_week = current_datetime.isoweekday()

        # Obtiene la hora actual
        current_time = current_datetime.time()

        # Filtrar los planes de trabajo por espacio_trabajo_id
        planes_trabajos = PlanTrabajo.objects.filter(espacio_id=espacio_trabajo_id, activo=True)
        if not planes_trabajos:
            return Response({"mensaje": "No se encontraron planes de trabajo activos para el espacio de trabajo proporcionado"}, status=status.HTTP_200_OK)

        # Obtener las PlanillaTrabajo asociadas a los planes de trabajo encontrados
        planillas = PlanillaTrabajo.objects.filter(plan_trabajo_id__in=planes_trabajos)
        if not planillas:
            return Response({"mensaje": "No se encontraron planillas de trabajo para el espacio de trabajo proporcionado"}, status=status.HTTP_200_OK)

        # Filtrar las planillas que contienen el número de día de la semana actual
        planillas_dia_actual = planillas.filter(dias_semana__contains=str(day_of_week))

        # Inicializar una lista de trabajadores que cumplen con el rango horario actual
        trabajadores = []

        # Iterar sobre las planillas y verificar el rango horario y el campo activo para cada trabajador
        for planilla in planillas_dia_actual:
            if (
                planilla.horario_inicio <= current_time <= planilla.horario_fin
                and planilla.trabajador.activo  # Verificar si el trabajador está activo
            ):
                trabajadores.append(planilla.trabajador)

        if not trabajadores:
            return Response({"mensaje": "No se encontraron trabajadores para el espacio de trabajo proporcionado. Verificar días de trabajo y horarios"}, status=status.HTTP_200_OK)

        serializer = TrabajadorSerializer(trabajadores, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)