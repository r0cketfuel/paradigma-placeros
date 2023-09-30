from django.urls                    import path
from apps.espacios_trabajo.views    import EspacioTrabajoListView, EspacioTrabajoRetrieveUpdateDestroyView, TrabajadoresAsignadosListView


urlpatterns = [
    path('',                                        EspacioTrabajoListView.as_view(),                   name='espacio-trabajo-list'),
    path('<int:pk>/',                               EspacioTrabajoRetrieveUpdateDestroyView.as_view(),  name='espacio-trabajo-detail'),
    path('trabajadores/<int:espacio_trabajo_id>/',  TrabajadoresAsignadosListView.as_view(),            name='trabajadores-asignados-list'),
]
