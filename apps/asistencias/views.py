from rest_framework             import viewsets
from .models                    import Asistencia
from .serializers               import AsistenciaSerializer
from apps.user_type.permisions  import IsAdministrador, IsSuper
import datetime


class AsistenciaViewSet(viewsets.ModelViewSet):

    queryset            = Asistencia.objects.all()
    serializer_class    = AsistenciaSerializer
    permission_classes  = [IsAdministrador | IsSuper]

    def get_queryset(self):
        # Obtén la fecha proporcionada en la consulta
        fecha = self.request.query_params.get('fecha', None)

        if fecha:
            # Filtra las asistencias por la fecha proporcionada
            queryset = Asistencia.objects.filter(fecha=fecha)
        else:
            # Si no se proporciona una fecha, muestra todas las asistencias
            queryset = Asistencia.objects.all()

        return queryset

    def perform_create(self, serializer):
        # Obtiene la fecha y hora actual
        now = datetime.datetime.now()
        # Establece la fecha y hora en el serializer antes de guardarlo
        serializer.save(fecha=now.date(), hora=now.time())
