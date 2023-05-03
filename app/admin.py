from django.contrib import admin
from .models import Bodega, Cliente,Comuna,Despacho,Libro,Tecnico,Mantencion,Pedido,SolicitudMant,Venta
from django import forms


admin.site.register(Bodega)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(Despacho)



admin.site.register(Libro)


admin.site.register(Tecnico)
admin.site.register(Mantencion)
admin.site.register(Pedido)
admin.site.register(SolicitudMant)
admin.site.register(Venta)