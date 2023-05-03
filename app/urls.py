from django.urls import path
from .views import *
from .views import login_view

urlpatterns = [
    path('', index, name="index"),

    path('contacto', contacto, name="contacto"),

    path('infoPublica', infoPublica, name="infoPublica"),

    path('productos', productos, name="productos"),

    path('login', login_view, name="login"),

    path('registrar', registrar, name="registrar"),
    
    path('base', base, name="base"),

]
