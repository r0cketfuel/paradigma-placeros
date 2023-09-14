from rest_framework             import viewsets
from rest_framework             import status
from rest_framework.response    import Response
from .models                    import Feriado
from .serializers               import FeriadoSerializer

class FeriadoViewSet(viewsets.ModelViewSet):
    serializer_class = FeriadoSerializer

    def get_queryset(self):
        try:
            queryset = Feriado.objects.all()
            year = self.request.query_params.get('ano')
            month = self.request.query_params.get('mes')
            day = self.request.query_params.get('dia')

            if year:
                year = int(year)
                queryset = queryset.filter(fecha__year=year)
            
            if month:
                month = int(month)
                queryset = queryset.filter(fecha__month=month)
            
            if day:
                day = int(day)
                queryset = queryset.filter(fecha__day=day)

            return queryset
        except ValueError:
            return Response({"error": "Uno o más parámetros no son números enteros válidos"}, status=status.HTTP_400_BAD_REQUEST)
