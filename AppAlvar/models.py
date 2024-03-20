from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.apellido} {self.nombre} -- Edad: {self.edad}"

class Proyecto(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    comercial = models.BooleanField(null=True, blank=True)
    imagen = models.ImageField(upload_to="proyectos", null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"Nombre: {self.nombre}"

class ProyectoFotos(models.Model):
    imagen = models.ImageField(upload_to="fotos")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="fotos")

opciones_consulta = [
    [0, 'Consulta'],
    [1, 'Cita'],
    [2, 'Presupuesto'],
    [3, 'Otro tipo']
]
class Consulta(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()

    def __str__(self):
        return f"Nombre:{self.nombre} -- {self.email}"


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True,blank=True)

    def __str__(self):
        return f"Avatar de {self.usuario}"