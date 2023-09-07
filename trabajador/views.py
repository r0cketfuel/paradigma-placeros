from rest_framework.response import Response
from rest_framework import viewsets
from .models import Trabajador
from .serializer import TrabajadorSerializer
from user_type.permisions import IsAdministrador, IsSuper


class TrabajadorViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar trabajadores.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    los registros de trabajadores. Los usuarios con permisos de administrador o superusuario
    pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase Trabajador.

    """
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAdministrador | IsSuper]


class TrabajadoresCargadosViewSet(viewsets.ViewSet):
    """
    Vista para obtener la cantidad de trabajadores cargados en la base de datos.

    Esta vista permite obtener la cantidad de registros de trabajadores existentes en la
    base de datos.

    Campos serializados:
    - 'trabajadores_cargados': Número de trabajadores cargados en la base de datos.

    """
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAdministrador | IsSuper]

    def list(self, request):
        trabajadores = Trabajador.objects.all()
        cargados = len(trabajadores) if trabajadores else 0
        return Response({"trabajadores_cargados": cargados}, status=200)
