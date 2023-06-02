from rest_framework import generics
from .models import LineaAmiga
from django.views.generic.base import TemplateView
from .serializers import ContentSerializer
from .models import LineaAmiga

class LineaAmigaList(generics.ListAPIView):
    queryset = LineaAmiga.objects.all()
    serializer_class = ContentSerializer

class LineaAmigaView(TemplateView):
    template_name = "lineaAmiga/lineaAmiga.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lineas'] = LineaAmiga.objects.all()
        return context