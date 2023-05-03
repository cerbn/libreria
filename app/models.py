# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bodega(models.Model):
    id_bodega = models.BigIntegerField(primary_key=True)
    direccion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bodega'


class Cliente(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    nombre_cli = models.CharField(max_length=30)
    segundo_nom_cli = models.CharField(max_length=30)
    primer_ap_cli = models.CharField(max_length=30)
    segundo_ap_cli = models.CharField(max_length=30)
    correo = models.CharField(max_length=60)
    edad = models.BigIntegerField()
    direccion = models.CharField(max_length=100)
    id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='id_comuna')

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.BigIntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'comuna'


class Despacho(models.Model):
    id_despacho = models.BigIntegerField(primary_key=True)
    fecha_despacho = models.DateField()
    direccion_despa = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'despacho'


class Libro(models.Model):
    id_libro = models.BigIntegerField(primary_key=True)
    nombre_libro = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    precio = models.BigIntegerField()
    stock = models.BigIntegerField()
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(editable=True,null=True, blank=True)
    id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='id_bodega')

    class Meta:
        managed = False
        db_table = 'libro'


class Mantencion(models.Model):
    id_mantencion = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    estado = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    id_solicitud = models.OneToOneField('SolicitudMant', models.DO_NOTHING, db_column='id_solicitud')
    id_tecnico = models.ForeignKey('Tecnico', models.DO_NOTHING, db_column='id_tecnico')

    class Meta:
        managed = False
        db_table = 'mantencion'


class Pedido(models.Model):
    id_pedido = models.BigIntegerField(primary_key=True)
    fecha_pedido = models.DateField()
    cantidad = models.BigIntegerField()
    precio_pedido = models.BigIntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='id_libro')

    class Meta:
        managed = False
        db_table = 'pedido'


class SolicitudMant(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    fecha_solicitud = models.DateField()
    descripcion_solic = models.CharField(max_length=130)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'solicitud_mant'


class Tecnico(models.Model):
    id_tecnico = models.BigIntegerField(primary_key=True)
    pnombre_tecnico = models.CharField(max_length=30)
    snombre_tecnico = models.CharField(max_length=30)
    apellidiop_tecnico = models.CharField(max_length=30)
    apellidom_tecnico = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tecnico'


class Venta(models.Model):
    id_venta = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    fecha_venta = models.DateField()
    id_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='id_libro')
    id_despacho = models.ForeignKey(Despacho, models.DO_NOTHING, db_column='id_despacho')

    class Meta:
        managed = False
        db_table = 'venta'
