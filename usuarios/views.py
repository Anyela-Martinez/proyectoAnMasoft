
from django.shortcuts import redirect, render
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario
from django.contrib import messages

# Create your views her

def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
}
    return render(request,'usuarios/usuarios.html',context) 

def adm_usuario(request):
    context={
    }
    return render(request, 'usuarios/adm-usuario.html', context)

def usuarios_crear(request):
    titulo="Usuarios - Crear"
    if request.method == "POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error")
    else:
        form=UsuarioForm()
    context={
        'titulo':titulo,
        'form':form
}
    return render(request,'usuarios/usuarios-crear.html',context) 

def login(request):
    context={
    }
    return render(request, 'usuarios/login.html', context)

def administradores(request):
    context={
    }
    return render(request, 'usuarios/administradores.html', context)

def administrar(request):
    context={
    }
    return render(request, 'usuarios/administrar.html', context)


