from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Services

# Create your views here.

class ServicesListView(ListView):
    model = Services

class ServicesDetailView(DetailView):
    model = Services