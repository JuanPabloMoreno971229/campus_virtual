from django.urls import path
from .views import HorarioList, ReservaCreate, VerDatos

urlpatterns = [
    path('horarios/', HorarioList.as_view()),
    path('reservas/', ReservaCreate.as_view()),
    path('ver-datos/', VerDatos.as_view(), name='ver-datos'),
]
