from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from servicios.models import Services
from usuario.models import User
from .forms import UserForm

def login(request):
    user_form = UserForm()
    # if request.method == "POST":
    #     user_form = UserForm(request.POST) 
    #     user= request.POST.get('user')
    #     passw= request.POST.get('password')
    #     if user_form.is_valid():
    #         for e in User.objects.all():
    #             if e.user == user:
    #                 for i in User.objects.all():
    #                     if i.password == passw:
    #                         global categoria 
    #                         categoria= User.objects.filter(user = e.user)
    #                         print(categoria)
    #                         return redirect('home')            
    context = {
        'form': user_form,
    }
    return render(request, "registration/login.html", context)

class HomePageView(TemplateView):
    template_name = "core/index.html"
    # categoria_home = {'categoria': categoria}
    # print(categoria_home)
    # servicios = Services.objects.all()
    # print(servicios)
    # usuario = User.objects.all()
    # context = {
    #     'user': usuario,
    #     'servicios': servicios,
    # }
    # return render(request, "core/index.html", context)

def servicios_details(request, id):
   print(id)
   servicios = Services.objects.filter(id=id)
   print(servicios)
   context = {
       'servicios' : servicios,
   }
   return render(request, "core/servicio_details.html", context) 