from rest_framework                 import viewsets
from .models                        import Asistencia
from .serializers                   import AsistenciaSerializer
from apps.user_type.permisions      import IsAdministrador, IsSuper
from apps.trabajadores.models       import Trabajador


class AsistenciaViewSet(viewsets.ModelViewSet):

    queryset            = Asistencia.objects.all()
    serializer_class    = AsistenciaSerializer
    permission_classes  = [IsAdministrador | IsSuper]
