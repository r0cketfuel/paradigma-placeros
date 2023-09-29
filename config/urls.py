from django.conf                            import settings
from django.conf.urls.static                import static
from django.urls                            import include, path
from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.views         import TokenRefreshView
from rest_framework                         import routers
from apps.users.views                       import UserRegisterationViewSet, UserLoginViewSet, UserLogoutViewSet
from apps.user_type.permisions              import IsSuper
from drf_yasg.views                         import get_schema_view
from drf_yasg                               import openapi
from apps.espacios_trabajo.views            import RutaUnoViewSet

# Importa los routers de las aplicaciones
from apps.asistencias.urls                  import router as asistencias_router
from apps.cooperativas.urls                 import router as cooperativas_router
from apps.cuestionarios.urls                import router as cuestionarios_router
from apps.dias_no_laborables.urls           import router as dias_no_laborables_router
from apps.espacios_trabajo.urls             import router as espacios_trabajo_router
from apps.evaluaciones_trabajadores.urls    import router as evaluaciones_trabajadores_router
from apps.evaluaciones_desempeño.urls       import router as evaluaciones_desempeño_router
from apps.feriados.urls                     import router as feriados_router
from apps.incidentes.urls                   import router as incidentes_router
from apps.planes_trabajo.urls               import router as planes_trabajo_router
from apps.planillas_trabajo.urls            import router as planillas_trabajo_router
from apps.respuestas_cuestionarios.urls     import router as respuestas_cuestionarios_router
from apps.trabajadores.urls                 import router as trabajadores_router
from apps.user_type.urls                    import router as user_type_router

# Define el esquema de documentación
schema_view = get_schema_view(
    openapi.Info(
        title           = 'Paradigma - Plaza Control API',
        default_version = 'v1.0',
        description     = 'Documentacion API REST para Paradigma - Plaza Control',
    ),
    public=True,
    permission_classes=[IsSuper],
)

# Define el router de nivel superior
router = routers.DefaultRouter()

# Registra los routers de las aplicaciones en el router de nivel superior
router.registry.extend(asistencias_router.registry)
router.registry.extend(cooperativas_router.registry)
router.registry.extend(cuestionarios_router.registry)
router.registry.extend(dias_no_laborables_router.registry)
router.registry.extend(espacios_trabajo_router.registry)
router.registry.extend(evaluaciones_trabajadores_router.registry)
router.registry.extend(evaluaciones_desempeño_router.registry)
router.registry.extend(feriados_router.registry)
router.registry.extend(incidentes_router.registry)
router.registry.extend(planes_trabajo_router.registry)
router.registry.extend(planillas_trabajo_router.registry)
router.registry.extend(respuestas_cuestionarios_router.registry)
router.registry.extend(trabajadores_router.registry)
router.registry.extend(user_type_router.registry)

router.register(r'user',        UserRegisterationViewSet,   basename='user')
router.register(r'login',       UserLoginViewSet,           basename='login')
router.register(r'logout',      UserLogoutViewSet,          basename='logout')

router.registry.sort(key=lambda x: x[0])

router.get_api_root_view().cls.__name__ = 'ParadigmaPlazaControlApiRoot'
router.get_api_root_view().cls.__doc__  = 'Documentacion en /snippets & /doc&test'
router.get_api_root_view().cls.permission_classes = [IsAuthenticated]

urlpatterns = [
    path('', include(router.urls)),
    path(r'snippets/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(r'doc&test/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('espacios_trabajo/trabajadores/<int:espacio_trabajo_id>', RutaUnoViewSet.as_view({'get': 'list'}), name='espacio_trabajo_trabajadores'),
    path('api-auth/', include('rest_framework.urls')),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
