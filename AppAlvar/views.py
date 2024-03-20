from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
#contrib.auth
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
#LoginRequired
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#-------------------USUARIOS---------------------#
#INICIAR SESION
def iniciar_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            usuario = authenticate(username=info_dict["username"],password=info_dict["password"])
            if usuario:
                login(request,usuario)
                messages.success(request, "Sesion Iniciada")
                return redirect(to="home")
        else:
            return render(request, "AppAlvar/home.html")
    
    else:
        formulario = AuthenticationForm()
    
    return render(request, "AppAlvar/registro/inicio_sesion.html", {'form':formulario})

#CERRAR SESION
@login_required
def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesion Finalizada")
    return redirect(to="home")

#REGISTRARSE
def registro(request):
    data = {
        'form': RegistroUsuario()
    }

    if request.method == "POST":
        formulario = RegistroUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='home')
        else:
            data['form'] = formulario
    
    return render(request, "AppAlvar/registro/registro.html", data)

#UPDATE
@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        formulario = EditarUsuario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario.email = info["email"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            messages.success(request, "Cambios Guardados")
            return redirect(to="home")
    else:
        formulario = EditarUsuario()
    return render(request, "AppAlvar/registro/editar_usuario.html", {"form":formulario})

#CAMBIAR CONTRASEÑA
class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppAlvar/registro/cambiar_contra.html"
    success_url = "/AppAlvar/"

#AVATAR
@login_required
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario_actual = User.objects.get(username=request.user)
            nuevo_avatar = Avatar(usuario=usuario_actual,imagen=info["imagen"])
            nuevo_avatar.save()
            messages.success(request, "Avatar Cambiado")
            return redirect(to="home")
    else:
        formulario = AvatarForm()
    
    return render(request, "AppAlvar/registro/nuevo_avatar.html", {"form":formulario})

#--------------------INICIO----------------------------
def home(request):
    return render(request, "AppAlvar/home.html")



#-----------------------CLIENTES-------------------------
#CREATE
@login_required
def agregar_cliente(request):
    data = {
        'form':ClienteForm()
    }

    if request.method == "POST":
        formulario =ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente creado")
            return redirect(to="cliente")
        else:
            data['form'] = formulario
            
    return render(request, 'AppAlvar/cliente/agregar.html', data)


#READ
@login_required
def ver_clientes(request):
    cliente = Cliente.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(cliente, 8)
        cliente = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':cliente,
        'paginator': paginator
    }

    return render(request, 'AppAlvar/cliente/ver.html', data)


#UPDATE
@login_required
def editar_cliente(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    data = {
        'form':ClienteForm(instance=cliente)
    }

    if request.method == "POST":
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="cliente")
        else:
            data['form'] = formulario

    return render(request, "AppAlvar/cliente/modificar.html", data)


#DELETE
@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, "Cliente eliminado correctamente")
    return redirect("cliente")


#-----------------------CONSULTAS---------------------------
#CREATE
def crear_consulta(request):
    data = {
        'form': ConsultaForm()
    }

    if request.method == "POST":
        formulario = ConsultaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Consulta creada")
            return redirect(to="crear_consulta")
        else:
            data['form'] = formulario
            
    return render(request, 'AppAlvar/consulta.html', data)


#READ
@login_required
def ver_consultas(request):
    consulta = Consulta.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(consulta, 8)
        consulta = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': consulta,
        'paginator': paginator
    }

    return render(request, 'AppAlvar/consulta/ver.html', data)


#UPDATE
@login_required
def editar_consulta(request,id):
    consulta = get_object_or_404(Consulta, id=id)
    data = {
        'form': ConsultaForm(instance=consulta)
    }

    if request.method == "POST":
        formulario = ConsultaForm(data=request.POST, instance=consulta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="ver_consulta")
        else:
            data['form'] = formulario

    return render(request, "AppAlvar/consulta/modificar.html", data)


#DELETE
@login_required
def eliminar_consulta(request,id):
    constulta = get_object_or_404(Consulta, id=id)
    constulta.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="ver_consulta")


#-----------------------PROYECTOS---------------------------
#CREATE
@login_required
def agregar_proyecto(request):
    data = {
        'form': ProyectoForm()
    }

    if request.method == "POST":
        formulario = ProyectoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proyecto Creado")
            return redirect(to="proyectos")
        else:
            data['form'] = formulario

    return render(request, "AppAlvar/proyecto/agregar.html", data)


#READ
def proyectos(request):
    proyectos = Proyecto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(proyectos, 8)
        proyectos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': proyectos,
        'paginator': paginator
    }

    return render(request, 'AppAlvar/proyectos.html', data)


#UPDATE
@login_required
def editar_proyecto(request,id):
    proyecto = get_object_or_404(Proyecto, id=id)
    data = {
        'form': ProyectoForm(instance=proyecto)
    }

    if request.method == "POST":
        formulario = ProyectoForm(data=request.POST, instance=proyecto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="proyectos")
        else:
            data['form'] = formulario

    return render(request, "AppAlvar/proyecto/modificar.html", data)


#DELETE
@login_required
def eliminar_proyecto(request,id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="proyectos")