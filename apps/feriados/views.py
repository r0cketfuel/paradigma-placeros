from rest_framework             import viewsets
from .models                    import Feriado
from .serializers               import FeriadoSerializer
from apps.user_type.permissions import IsAdministrador, IsSuper


class FeriadoViewSet(viewsets.ModelViewSet):
    serializer_class    = FeriadoSerializer
    permission_classes  = [IsAdministrador | IsSuper]

    def get_queryset(self):
        queryset    = Feriado.objects.all()
        year        = self.request.query_params.get('ano')
        month       = self.request.query_params.get('mes')
        day         = self.request.query_params.get('dia')

        if year:
            year        = int(year)
            queryset    = queryset.filter(fecha__year=year)
        
        if month:
            month       = int(month)
            queryset    = queryset.filter(fecha__month=month)
        
        if day:
            day         = int(day)
            queryset    = queryset.filter(fecha__day=day)

        return queryset