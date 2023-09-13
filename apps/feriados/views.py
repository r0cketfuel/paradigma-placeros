# views.py

from rest_framework import viewsets
from .models import Feriado
from .serializers import FeriadoSerializer
from apps.user_type.permisions import IsAdministrador, IsSuper


class FeriadoViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar feriados.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    los registros de feriados. Los usuarios con permisos de administrador o superusuario
    pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase Feriado.

    """
    queryset = Feriado.objects.all()
    serializer_class = FeriadoSerializer
    permission_classes = [IsAdministrador | IsSuper]
