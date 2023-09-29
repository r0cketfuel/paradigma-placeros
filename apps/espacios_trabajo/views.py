from rest_framework                 import viewsets

from apps.trabajadores.models import Trabajador
from .models                        import EspacioTrabajo
from .serializer                    import EspacioTrabajoSerializer
from apps.user_type.permisions      import IsAdministrador, IsSuper, IsSupervisor
from apps.planillas_trabajo.models  import PlanillaTrabajo
from apps.planillas_trabajo.serializer import PlanillaTrabajoSerializer
from apps.trabajadores.serializer import TrabajadorSerializer
from rest_framework.response        import Response

from apps.planes_trabajo.models     import PlanTrabajo

class EspacioTrabajoViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar espacios de trabajo.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en
    los espacios de trabajo. Los usuarios con permisos de administrador o superusuario
    pueden acceder a esta vista.

    Campos serializados:
    - Todos los campos de la clase EspacioTrabajo.

    """
    queryset = EspacioTrabajo.objects.all()
    serializer_class = EspacioTrabajoSerializer
    permission_classes = [IsAdministrador | IsSuper]


# class RutaUnoViewSet(viewsets.ModelViewSet):

#     queryset            = PlanillaTrabajo.objects.all()
#     serializer_class    = PlanillaTrabajo
#     permission_classes  = [IsAdministrador | IsSuper | IsSupervisor]

#     def list(self,request, espacio_trabajo_id=None):
#         # planilla<-plan<-espacio
#         planes_trabajos=PlanTrabajo.objects.filter(espacio=espacio_trabajo_id)
#         # print(planes_trabajos)
#         # print(PlanillaTrabajo.objects.all())
#         lista= []
#         for planilla in PlanillaTrabajo.objects.all():
#             for plan in planes_trabajos:
#                 # print("plan:",plan.__dict__)
#                 # print("planilla: ", planilla.__dict__)
#                 if planilla.plan_trabajo_id == plan.id:                    
#                     lista.append(Trabajador.objects.get(id=planilla.trabajador_id).id)
#         return Response(data = {'lista':lista} , status=200)

class RutaUnoViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all() 
    serializer_class = TrabajadorSerializer  # Cambiar al serializador de Trabajador
    permission_classes = [IsAdministrador | IsSuper | IsSupervisor]

    def list(self, request, espacio_trabajo_id=None):
        # Filtrar los planes de trabajo por espacio_trabajo_id
        planes_trabajos = PlanTrabajo.objects.filter(espacio_id=espacio_trabajo_id)

        # Obtener las PlanillaTrabajo asociadas a los planes de trabajo encontrados
        planillas = PlanillaTrabajo.objects.filter(plan_trabajo_id__in=planes_trabajos)

        # Obtener la lista de trabajadores asociados a las PlanillaTrabajo encontradas
        lista_trabajadores = [planilla.trabajador_id for planilla in planillas]

        # Obtener los detalles de los trabajadores
        trabajadores = Trabajador.objects.filter(id__in=lista_trabajadores)
        serializer = TrabajadorSerializer(trabajadores, many=True)

        return Response(serializer.data, status=200)
