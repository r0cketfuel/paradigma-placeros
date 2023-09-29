from    rest_framework              import viewsets, status
from    rest_framework.response     import Response
from    .models                     import Asistencia
from    .serializers                import AsistenciaSerializer
from    apps.user_type.permisions   import IsAdministrador, IsSuper
from    datetime                    import datetime
from    django.db.models            import Q
from    datetime                    import date
import  pytz


class AsistenciaViewSet(viewsets.ModelViewSet):

    serializer_class    = AsistenciaSerializer
    permission_classes  = [IsAdministrador | IsSuper]
    
    def get_queryset(self):
        queryset = Asistencia.objects.all()

        # Obtener las fechas de consulta desde los parámetros de la solicitud
        fecha_desde_str = self.request.query_params.get('fecha_desde', None)
        fecha_hasta_str = self.request.query_params.get('fecha_hasta', None)

        # Convierte las cadenas de fecha en objetos datetime si están presentes
        if fecha_desde_str:
            fecha_desde = datetime.strptime(fecha_desde_str, '%Y-%m-%d').replace(tzinfo=pytz.UTC)
        else:
            # Si fecha_desde no se proporciona, establecerlo en el inicio del día actual
            fecha_desde = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=pytz.UTC)

        if fecha_hasta_str:
            fecha_hasta = datetime.strptime(fecha_hasta_str, '%Y-%m-%d').replace(tzinfo=pytz.UTC)
            # Establece la hora en 23:59:59 para incluir toda la fecha actual
            fecha_hasta = fecha_hasta.replace(hour=23, minute=59, second=59)
        else:
            # Si fecha_hasta no se proporciona, establecerlo en el final del día actual
            fecha_hasta = datetime.combine(date.today(), datetime.max.time()).replace(tzinfo=pytz.UTC)

        # Aplicar el filtro de fecha para incluir toda la fecha actual
        queryset = queryset.filter(Q(fecha__gte=fecha_desde) & Q(fecha__lte=fecha_hasta))

        return queryset


    def create(self, request, *args, **kwargs):
        data = request.data
        is_list = isinstance(data, list)

        if is_list:
            asistencias_creadas = []
            for item in data:
                serializer = AsistenciaSerializer(data=item)
                if serializer.is_valid():                
                    serializer.save()
                    asistencias_creadas.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(asistencias_creadas, status=status.HTTP_201_CREATED)
        else:
            serializer = AsistenciaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
