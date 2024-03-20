from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ProyectoFotosForm(forms.ModelForm):
    class Meta:
        model = ProyectoFotos
        fields = ['imagen']

class RegistroUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']

class EditarUsuario(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["email","first_name","last_name"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
        }

class AvatarForm(forms.Form):
    imagen = forms.ImageField()