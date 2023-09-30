from django.urls                    import path, include
from rest_framework.routers         import DefaultRouter
from apps.dias_no_laborables.views  import DiaNoLaborableViewSet


router = DefaultRouter()
router.register(r'dias_no_laborables', DiaNoLaborableViewSet, basename='dias_no_laborables')

urlpatterns = [
    path('', include(router.urls)),
]
