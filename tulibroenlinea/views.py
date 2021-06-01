from django.http import HttpResponseRedirect
#from django.template import Template, Context
#from django.template.loader import get_template
from django.shortcuts import render
from aplicacion.models import *

usuario_global = []

def usobase(request):
    nombre = "Tu libro en linea"
    return render(request, 'usobase.html', {"nombre":nombre})

def inicio(request):
    nombre = "inicio"
    return render(request, 'inicio.html', {"nombre":nombre})

def inicio2(request):
    usuario = request.GET["usuario"]
    contrasena =  request.GET["contrasena"]
    usu = Usuario.objects.filter(usuario = usuario, contrasena = contrasena)
    if usu:
        if usu[0].tipo == "root":
            return HttpResponseRedirect("/moduloRoot/")
        elif usu[0].tipo == "admin":
            return HttpResponseRedirect("/moduloAdmin/")
        elif usu[0].tipo == "cliente":
            return HttpResponseRedirect("/moduloUsuario/")
    usuario_global.append(usuario)
    usuario_global.append(contrasena)


def registro(request):
    nombre = "Crear Usuario"
    return render(request, 'registro.html', {"nombre":nombre})
    
def registro2(request):
    nombre = "Crear Usuario"
    nombre_usuario = request.GET["nombre"]
    apellido_usuario = request.GET["apellido"]
    dni_usuario = request.GET["dni"]
    correo_usuario = request.GET["correo"]
    fecha_usuario = request.GET["fecha"]
    sexo_usuario = request.GET["sexo"]
    lugar_usuario = request.GET["lugar"]
    direccion_usuario = request.GET["direccion"]
    usuario_usuario = request.GET["usuario"]
    contrasena_usuario = request.GET["contrasena"]
    cli = Cliente(dni_usuario,usuario_usuario, contrasena_usuario, "cliente", nombre_usuario, apellido_usuario, dni_usuario, fecha_usuario, lugar_usuario, direccion_usuario, sexo_usuario, correo_usuario, " ", " ", False, False, False, None, " ")
    usu = Usuario(dni_usuario,usuario_usuario, contrasena_usuario, "cliente")
    cli.save()
    usu.save()
    return HttpResponseRedirect('https://tleladn.herokuapp.com/')  

def moduloRoot(request):
    nombre = "Modulo Root"
    return render(request, 'moduloRoot.html', {"nombre":nombre})

def moduloRoot_crearAdmin(request):
    nombre = "Crear Administrador"
    return render(request, 'moduloRoot_crearAdmin.html', {"nombre":nombre})

def moduloRoot_genInforme(request):
    nombre = "Generar informe"
    return render(request, 'moduloRoot_genInforme.html', {"nombre":nombre})

def moduloAdmin(request):
    nombre = "Modulo Admin"
    return render(request, 'moduloAdmin.html', {"nombre":nombre})

def moduloAdmin_Usuario_Crear(request):
    nombre = "Crear Usuario"
    return render(request, 'moduloAdmin_Usuario_Crear.html', {"nombre":nombre})
    
def moduloAdmin_Usuario_Crear2(request):
    nombre = "Crear Usuario"
    nombre_usuario = request.GET["nombre"]
    apellido_usuario = request.GET["apellido"]
    dni_usuario = request.GET["dni"]
    correo_usuario = request.GET["correo"]
    fecha_usuario = request.GET["fecha"]
    sexo_usuario = request.GET["sexo"]
    lugar_usuario = request.GET["lugar"]
    direccion_usuario = request.GET["direccion"]
    usuario_usuario = request.GET["usuario"]
    contrasena_usuario = request.GET["contrasena"]
    cli = Cliente(dni_usuario,usuario_usuario, contrasena_usuario, "cliente", nombre_usuario, apellido_usuario, dni_usuario, fecha_usuario, lugar_usuario, direccion_usuario, sexo_usuario, correo_usuario, correo_usuario, correo_usuario, True, True)
    usu = Usuario(dni_usuario,usuario_usuario, contrasena_usuario, "cliente")
    cli.save()
    usu.save()
    noti = True
    return render(request, 'moduloAdmin_Usuario_Crear.html', {"nombre":nombre, "noti":noti})
    
def moduloAdmin_Usuario_Modificar(request):
    nombre = "Modificar Usuario"
    return render(request, 'moduloAdmin_Usuario_Modificar.html', {"nombre":nombre})

def moduloAdmin_Usuario_Modificar2(request):
    nombre = "Modificar Usuario"
    dni = request.GET["dni"]
    cli = Cliente.objects.filter(idUsuario = dni)
    nombre_usuario = cli[0].nombres
    apellido_usuario = cli[0].apellidos
    dni_usuario = cli[0].dni
    correo_usuario = cli[0].correo
    fecha_usuario = cli[0].fechaN
    sexo_usuario = cli[0].genero
    lugar_usuario = cli[0].lugarN
    direccion_usuario = cli[0].direccion
    usuario_usuario = cli[0].usuario
    contrasena_usuario = cli[0].contrasena
    return render(request, 'moduloAdmin_Usuario_Modificar.html', {"nombre":nombre, "nombre_usuario":nombre_usuario, "apellido_usuario":apellido_usuario, "dni_usuario":dni_usuario, "correo_usuario":correo_usuario, "fecha_usuario":fecha_usuario, "sexo_usuario":sexo_usuario, "lugar_usuario":lugar_usuario, "direccion_usuario":direccion_usuario, "usuario_usuario":usuario_usuario, "contrasena_usuario":contrasena_usuario})

def moduloAdmin_Usuario_Modificar3(request):
    nombre = "Modificar Usuario"
    nombre_usuario = request.GET["nombre"]
    apellido_usuario = request.GET["apellido"]
    dni_usuario = request.GET["dni"]
    correo_usuario = request.GET["correo"]
    fecha_usuario = request.GET["fecha"]
    sexo_usuario = request.GET["sexo"]
    lugar_usuario = request.GET["lugar"]
    direccion_usuario = request.GET["direccion"]
    usuario_usuario = request.GET["usuario"]
    contrasena_usuario = request.GET["contrasena"]
    cli = Cliente(dni_usuario,usuario_usuario, contrasena_usuario, "cliente", nombre_usuario, apellido_usuario, dni_usuario, fecha_usuario, lugar_usuario, direccion_usuario, sexo_usuario, correo_usuario, "", "", True, True)
    cli.save()
    noti = True
    return render(request, 'moduloAdmin_Usuario_Modificar.html', {"nombre":nombre, "noti": noti})

def moduloAdmin_Usuario_Listar(request):
    nombre = "Listar Usuarios"
    return render(request, 'moduloAdmin_Usuario_Listar.html', {"nombre":nombre})

def moduloAdmin_Usuario_Buscar(request):
    nombre = "Buscar Usuario"
    return render(request, 'moduloAdmin_Usuario_Buscar.html', {"nombre":nombre})

def moduloAdmin_Usuario_Buscar2(request):
    nombre = "Buscar Usuario"
    dni = request.GET["dni"]
    cli = Cliente.objects.filter(idUsuario = dni)
    nombre_usuario = cli[0].nombres
    apellido_usuario = cli[0].apellidos
    dni_usuario = cli[0].dni
    correo_usuario = cli[0].correo
    fecha_usuario = cli[0].fechaN
    sexo_usuario = cli[0].genero
    lugar_usuario = cli[0].lugarN
    direccion_usuario = cli[0].direccion
    usuario_usuario = cli[0].usuario
    contrasena_usuario = cli[0].contrasena
    return render(request, 'moduloAdmin_Usuario_Buscar.html', {"nombre":nombre, "nombre_usuario":nombre_usuario, "apellido_usuario":apellido_usuario, "dni_usuario":dni_usuario, "correo_usuario":correo_usuario, "fecha_usuario":fecha_usuario, "sexo_usuario":sexo_usuario, "lugar_usuario":lugar_usuario, "direccion_usuario":direccion_usuario, "usuario_usuario":usuario_usuario, "contrasena_usuario":contrasena_usuario})

def moduloAdmin_Usuario_Eliminar(request):
    nombre = "Eliminar Usuario"
    return render(request, 'moduloAdmin_Usuario_Eliminar.html', {"nombre":nombre})

def moduloAdmin_Usuario_Eliminar2(request):
    nombre = "Eliminar Usuario"
    dni = request.GET["dni"]
    cli = Cliente.objects.filter(idUsuario = dni)
    nombre_usuario = cli[0].nombres
    apellido_usuario = cli[0].apellidos
    dni_usuario = cli[0].dni
    correo_usuario = cli[0].correo
    fecha_usuario = cli[0].fechaN
    sexo_usuario = cli[0].genero
    lugar_usuario = cli[0].lugarN
    direccion_usuario = cli[0].direccion
    usuario_usuario = cli[0].usuario
    contrasena_usuario = cli[0].contrasena
    return render(request, 'moduloAdmin_Usuario_Eliminar.html', {"nombre":nombre, "nombre_usuario":nombre_usuario,"apellido_usuario":apellido_usuario, "dni_usuario":dni_usuario, "correo_usuario":correo_usuario, "fecha_usuario":fecha_usuario, "sexo_usuario":sexo_usuario, "lugar_usuario":lugar_usuario, "direccion_usuario":direccion_usuario, "usuario_usuario":usuario_usuario, "contrasena_usuario":contrasena_usuario})

def moduloAdmin_Usuario_Eliminar3(request):
    nombre = "Eliminar Usuario"
    dni = request.GET["dni"]
    cli = Cliente.objects.filter(idUsuario = dni)
    usu = Usuario.objects.filter(idUsuario = dni)
    cli.delete()
    usu.delete()
    noti = True
    return render(request, 'moduloAdmin_Usuario_Eliminar.html', {"nombre":nombre, "noti": noti})

def moduloAdmin_Libro_Crear(request):
    nombre = "Crear Libro"
    return render(request, 'moduloAdmin_Libro_Crear.html', {"nombre":nombre})

def moduloAdmin_Libro_Modificar(request):
    nombre = "Modificar Libro"
    return render(request, 'moduloAdmin_Libro_Modificar.html', {"nombre":nombre})

def moduloAdmin_Libro_Listar(request):
    nombre = "Listar Libros"
    return render(request, 'moduloAdmin_Libro_Listar.html', {"nombre":nombre})

def moduloAdmin_Libro_Buscar(request):
    nombre = "Buscar Libro"
    return render(request, 'moduloAdmin_Libro_Buscar.html', {"nombre":nombre})

def moduloAdmin_Libro_Eliminar(request):
    nombre = "Eliminar Libro"
    return render(request, 'moduloAdmin_Libro_Eliminar.html', {"nombre":nombre})

def moduloAdmin_Compra_Historico(request):
    nombre = "Historico Compras"
    return render(request, 'moduloAdmin_Compra_Historico.html', {"nombre":nombre})

def moduloAdmin_Compra_HistoricoCanc(request):
    nombre = "Historico de cancelaciones de Compras"
    return render(request, 'moduloAdmin_Compra_HistoricoCanc.html', {"nombre":nombre})

def moduloAdmin_Reserva_Historico(request):
    nombre = "Historico Reservas"
    return render(request, 'moduloAdmin_Reserva_Historico.html', {"nombre":nombre})

def moduloAdmin_Reserva_HistoricoCanc(request):
    nombre = "Historico de cancelaciones de Reservas"
    return render(request, 'moduloAdmin_Reserva_HistoricoCanc.html', {"nombre":nombre})

def moduloAdmin_Devolucion_Atender(request):
    nombre = "Atender devolucion"
    return render(request, 'moduloAdmin_Devolucion_Atender.html', {"nombre":nombre})

def moduloAdmin_Devolucion_Historico(request):
    nombre = "Historico Devoluciones"
    return render(request, 'moduloAdmin_devolucion_Historico.html', {"nombre":nombre})

def moduloUsuario(request):
    nombre = "Modulo Usuario"
    return render(request, 'moduloUsuario.html', {"nombre":nombre})

def moduloUsuario_Usuario_Modificar(request):
    nombre = "Modificar Usuario"
    return render(request, 'moduloUsuario_Usuario_Modificar.html', {"nombre":nombre})

def moduloUsuario_Usuario_Modificar2(request):
    nombre = "Modificar Usuario"
    usuario = request.GET["usuario"]
    contrasena = request.GET["contrasena"]
    cli = Cliente.objects.filter(usuario = usuario, contrasena = contrasena)
    if cli:
        nombre_usuario = cli[0].nombres
        apellido_usuario = cli[0].apellidos
        dni_usuario = cli[0].dni
        correo_usuario = cli[0].correo
        fecha_usuario = cli[0].fechaN
        sexo_usuario = cli[0].genero
        lugar_usuario = cli[0].lugarN
        direccion_usuario = cli[0].direccion
        usuario_usuario = cli[0].usuario
        contrasena_usuario = cli[0].contrasena
    else: 
        pass
    return render(request, 'moduloUsuario_Usuario_Modificar.html', {"nombre":nombre, "nombre_usuario":nombre_usuario, "apellido_usuario":apellido_usuario, "dni_usuario":dni_usuario, "correo_usuario":correo_usuario, "fecha_usuario":fecha_usuario, "sexo_usuario":sexo_usuario, "lugar_usuario":lugar_usuario, "direccion_usuario":direccion_usuario, "usuario_usuario":usuario_usuario, "contrasena_usuario":contrasena_usuario})

def moduloUsuario_Usuario_Modificar3(request):
    nombre = "Modificar Usuario"
    nombre_usuario = request.GET["nombre"]
    apellido_usuario = request.GET["apellido"]
    dni_usuario = request.GET["dni"]
    correo_usuario = request.GET["correo"]
    fecha_usuario = request.GET["fecha"]
    sexo_usuario = request.GET["sexo"]
    lugar_usuario = request.GET["lugar"]
    direccion_usuario = request.GET["direccion"]
    usuario_usuario = request.GET["usuario"]
    contrasena_usuario = request.GET["contrasena"]
    cli = Cliente(dni_usuario,usuario_usuario, contrasena_usuario, "cliente", nombre_usuario, apellido_usuario, dni_usuario, fecha_usuario, lugar_usuario, direccion_usuario, sexo_usuario, correo_usuario)
    cli.save()
    noti = True
    return render(request, 'moduloUsuario_Usuario_Modificar.html', {"nombre":nombre, "noti": noti})

def moduloUsuario_Usuario_Eliminar(request):
    nombre = "Eliminar Usuario"
    return render(request, 'moduloUsuario_Usuario_Eliminar.html', {"nombre":nombre})

def moduloUsuario_Usuario_Eliminar2(request):
    nombre = "Eliminar Usuario"
    usuario = request.GET["usuario"]
    contrasena = request.GET["contrasena"]
    cli = Cliente.objects.filter(usuario = usuario, contrasena = contrasena)
    usu = Usuario.objects.filter(usuario = usuario)
    if cli:
        cli.delete()
        usu.delete()
    else:
        pass
    return HttpResponseRedirect(" ") 
    
def moduloUsuario_Perfil_Crear(request):
    nombre = "Crear Perfil"
    return render(request, 'moduloUsuario_Perfil_Crear.html', {"nombre":nombre})

def moduloUsuario_Perfil_Crear2(request):

    nombre = "Crear Perfil"

    cli = Cliente.objects.filter(usuario = usuario_global[0], contrasena = usuario_global[1])
    foto_usuario = request.GET["foto"]
    desc_usuario = request.GET["desc"]
    perfil_usuario = True
    noti_usuario = request.GET["noti"]
    msj_usuario = request.GET["msj"]

    clinuevo = Cliente(cli[0].dni, cli[0].usuario, cli[0].contrasena, cli[0].tipo, cli[0].nombres, cli[0].apellidos, cli[0].dni, cli[0].fechaN, cli[0].lugarN, cli[0].direccion, cli[0].genero, cli[0].correo, " ", " ", noti_usuario, msj_usuario, perfil_usuario, foto_usuario, desc_usuario)
    clinuevo.save()
    
    return render(request, 'moduloUsuario_Perfil_Crear.html', {"nombre":nombre})

def moduloUsuario_Perfil_Modificar(request):
    nombre = "Modificar Perfil"
    return render(request, 'moduloUsuario_Perfil_Modificar.html', {"nombre":nombre})

def moduloUsuario_Perfil_Modificar2(request):
    nombre = "Modificar Perfil"
    usuario = request.GET["usuario"]
    contrasena = request.GET["contrasena"]
    cli = Cliente.objects.filter(usuario = usuario, contrasena = contrasena)
    if cli:
        nombre_usuario = cli[0].nombres
        apellido_usuario = cli[0].apellidos
        dni_usuario = cli[0].dni
    else: 
        pass
    return render(request, 'moduloUsuario_Perfil_Modificar.html', {"nombre":nombre})

def moduloUsuario_Perfil_Modificar3(request):
    nombre = "Modificar Perfil"
    return render(request, 'moduloUsuario_Perfil_Modificar.html', {"nombre":nombre})

def moduloUsuario_Usuario_Mensajeria(request):
    nombre = "Modificar Usuario"
    return render(request, 'moduloUsuario_Usuario_Mensajeria.html', {"nombre":nombre})