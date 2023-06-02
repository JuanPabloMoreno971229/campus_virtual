from django.urls import include, path
from rest_framework import routers
from .views import LineaAmigaList, LineaAmigaView

urlpatterns = [
     path('linea-amiga/', LineaAmigaList.as_view()),
     path('linea-Amiga/', LineaAmigaView.as_view()),
]

