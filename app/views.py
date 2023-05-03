from email.headerregistry import Group
from multiprocessing.sharedctypes import Value
from re import A
from unicodedata import name
import requests
from django.shortcuts import get_object_or_404, redirect, render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from app.forms import ProductoForm
from .forms import *
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView
from .forms import LoginForm





# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def infoPublica(request):
    return render(request, 'app/infoPublica.html')


def productos(request):
    libro = Libro.objects.all
    data = {
        'libro' : libro
    }
    return render(request, 'app/productos.html', data)


def registrar(request):
    datos = {
        'form' : RegistroUsuarioForm() }
        
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            groups = Group.objects.get(name="cliente")
            user.groups.add(groups)
            usuario = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            messages.success(request,'usuario guardado correctamente!')
    return render(request, 'app/registrar.html', datos)




def base(request):
    return render(request, 'app/base.html')



def login1(request):
    return render(request, 'app/login1.html')





def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app/login.index')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})