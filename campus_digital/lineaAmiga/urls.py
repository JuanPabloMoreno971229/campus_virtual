from django.urls import include, path
from rest_framework import routers
from .views import LineaAmigaList

urlpatterns = [
     path('linea-amiga/', LineaAmigaList.as_view()),
]

