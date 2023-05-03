from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
 
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nombre', help_text='')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido', help_text='')
    email = forms.EmailField(max_length=254, required=True, label='Correo electrónico', help_text='')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, help_text='')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
        }
        error_messages = {
            'username': {
                'unique': 'Ya existe un usuario con este nombre de usuario. Por favor, elige otro.',
            },
        }
        help_texts = {
            'username': '',
        }




class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(label="Contraseña", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))




class ProductoForm(ModelForm):
    
    class Meta:
        model = Libro
        fields = "__all__"


    class Meta:
        model = Libro
        fields = ['id_libro','nombre_libro','autor','precio','stock','descripcion','imagen']



        #widgets = {
         #   'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        #}
