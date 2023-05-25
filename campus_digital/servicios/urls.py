from django.urls import path
from .views import ServicesListView, ServicesDetailView

app_name = 'servicios'

urlpatterns = [
    path('servicios/', ServicesListView.as_view(), name="servicios"),
    path('<int:pk>/<slug:Services_slug>/', ServicesDetailView.as_view(), name="servicios_detalles"),
]