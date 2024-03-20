from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    #Usuario
    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("logout/", cerrar_sesion, name="cerrar_sesion"),
    path("registro/", registro, name="registro"),
    path("edit/", editar_usuario, name="editar_usuario"),
    path("contra/", CambiarContra.as_view(), name="cambiar_contraseña"),
    #imagenes
    path("avatar/", agregar_avatar, name="add_avatar"),

    #clientes
    path('cliente/', ver_clientes, name="cliente"),
    path('agregar_cliente/', agregar_cliente, name="agregar_cliente"),
    path('editar_cliente/<id>', editar_cliente, name="editar_cliente"),
    path('eliminar_cliente/<int:id>/', eliminar_cliente, name='eliminar_cliente'),


    #consultas
    path('ver_consulta/', ver_consultas, name="ver_consulta"),
    path('consulta/', crear_consulta, name="crear_consulta"),
    path('editar_consulta/<id>', editar_consulta, name="editar_consulta"),
    path('eliminar_consulta/<int:id>', eliminar_consulta, name="eliminar_consulta"),

    #proyectos
    path('proyectos/', proyectos, name="proyectos"),
    path('agregar_proyecto/', agregar_proyecto, name="agregar_proyecto"),
    path('editar_proyecto/<id>/', editar_proyecto, name="editar_proyecto"),
    path('eliminar_proyecto/<int:id>/', eliminar_proyecto, name="eliminar_proyecto"),
]