from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from servicios.models import Services
from usuario.models import User
from .forms import UserForm

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kargs):
        servicios = Services.objects.all()
        context = {
            'servicios': servicios 
        }
        return render(request, self.template_name, context)
