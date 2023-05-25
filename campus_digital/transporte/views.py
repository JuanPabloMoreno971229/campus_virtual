from rest_framework import generics
from .models import Horario, Reserva
from .serializers import HorarioSerializer, ReservaSerializer
from django.shortcuts import render
from django.views import View
import requests

class HorarioList(generics.ListAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class ReservaCreate(generics.CreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class VerDatos(View):
    def get(self, request):
        return render(request, 'transporte/transporte.html')


