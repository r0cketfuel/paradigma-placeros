# views.py en la app 'asistencias'
from    rest_framework              import viewsets, status
from    rest_framework.response     import Response
from    .models                     import Asistencia
from    .serializers                import AsistenciaSerializer
from    apps.user_type.permissions  import IsAdministrador, IsSuper
from    datetime                    import datetime
from    django.db.models            import Q
from    datetime                    import date
import  pytz

class AsistenciaTrabajadorViewSet(viewsets.ModelViewSet):
    serializer_class = AsistenciaSerializer
    permission_classes = [IsAdministrador | IsSuper]
    
    def get_queryset(self):
        queryset = Asistencia.objects.all()

        fecha_desde_str     = self.request.query_params.get('fecha_desde', None)
        fecha_hasta_str     = self.request.query_params.get('fecha_hasta', None)
        espacio_trabajo_id  = self.request.query_params.get('espacio_trabajo', None)

        if fecha_desde_str:
            fecha_desde = datetime.strptime(fecha_desde_str, '%Y-%m-%d').replace(tzinfo=pytz.UTC)
        else:
            fecha_desde = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=pytz.UTC)

        if fecha_hasta_str:
            fecha_hasta = datetime.strptime(fecha_hasta_str, '%Y-%m-%d').replace(tzinfo=pytz.UTC)
            fecha_hasta = fecha_hasta.replace(hour=23, minute=59, second=59)
        else:
            fecha_hasta = datetime.combine(date.today(), datetime.max.time()).replace(tzinfo=pytz.UTC)

        queryset = queryset.filter(Q(fecha__gte=fecha_desde) & Q(fecha__lte=fecha_hasta))

        if espacio_trabajo_id:
            queryset = queryset.filter(espacio_trabajo_id=espacio_trabajo_id)

        queryset = queryset.select_related('espacio_trabajo')

        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        is_list = isinstance(data, list)

        if is_list:
            asistencias_creadas = []
            for item in data:
                serializer = AsistenciaSerializer(data=item)
                if serializer.is_valid():
                    espacio_trabajo_id = item.get('espacio_trabajo')
                    serializer.save(espacio_trabajo_id=espacio_trabajo_id)
                    asistencias_creadas.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(asistencias_creadas, status=status.HTTP_201_CREATED)
        else:
            serializer = AsistenciaSerializer(data=data)
            if serializer.is_valid():
                espacio_trabajo_id = data.get('espacio_trabajo')
                serializer.save(espacio_trabajo_id=espacio_trabajo_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)