from rest_framework import generics
from .models import LineaAmiga
from .serializers import ContentSerializer

class LineaAmigaList(generics.ListAPIView):
    queryset = LineaAmiga.objects.all()
    serializer_class = ContentSerializer
