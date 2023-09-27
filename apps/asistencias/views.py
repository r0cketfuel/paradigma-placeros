from rest_framework             import viewsets, status
from rest_framework.response    import Response
from .models                    import Asistencia
from .serializers               import AsistenciaSerializer
from apps.user_type.permisions  import IsAdministrador, IsSuper


class AsistenciaViewSet(viewsets.ModelViewSet):

    queryset            = Asistencia.objects.all()
    serializer_class    = AsistenciaSerializer
    permission_classes  = [IsAdministrador | IsSuper]
    
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
