from django.http import HttpResponseRedirect
from django.shortcuts import render
from aplicacion.models import *

usuario_global = []
cliente_global = []

def usobase(request):
    nombre = "Tu libro en linea"
    return render(request, 'usobase.html', {"nombre":nombre})

def inicio(request):
    nombre = "inicio"
    return render(request, 'inicio.html', {"nombre":nombre})

def inicio2(request):
    nombre = "inicio"
    usuario = request.GET["usuario"]
    contrasena =  request.GET["contrasena"]
    usu = Usuario.objects.filter(usuario = usuario, contrasena = contrasena)
    if usu:
        usuario_global.append(usuario)
        usuario_global.append(contrasena)
        if usu[0].tipo == "root":
            return HttpResponseRedirect("/moduloRoot/")
        elif usu[0].tipo == "admin":
            return HttpResponseRedirect("/moduloAdmin/")
        elif usu[0].tipo == "cliente":
            cli = Cliente.objects.filter(usuario = usuario_global[0], contrasena = usuario_global[1])
            usuario_global.append(cli[0].perfil)
            cliente_global.append(cli[0].temas)
            cliente_global.append(cli[0].top)
            cliente_global.append(cli[0].suscripcion)
            cliente_global.append(cli[0].mensajeria)
            cliente_global.append(cli[0].perfil)
            cliente_global.append(cli[0].foto)
            cliente_global.append(cli[0].descripcion)
            return HttpResponseRedirect("/moduloUsuario/")
    else:
        noti = True
        return render(request, 'inicio.html', {"nombre":nombre, "noti": noti})
        
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

def moduloRoot_crearAdmin2(request):
    nombre = "Crear Administrador"
    nombre_admin = request.GET["nombre"]
    apellido_admin = request.GET["apellido"]
    dni_admin = request.GET["dni"]
    correo_admin = request.GET["correo"]
    fecha_admin = request.GET["fecha"]
    sexo_admin = request.GET["sexo"]
    lugar_admin = request.GET["lugar"]
    direccion_admin = request.GET["direccion"]
    usuario_admin = request.GET["usuario"]
    contrasena_admin = request.GET["contrasena"]
    adm = Administrador(dni_admin,usuario_admin, contrasena_admin, "admin", nombre_admin, apellido_admin, dni_admin, fecha_admin, lugar_admin, direccion_admin, sexo_admin, correo_admin)
    usu = Usuario(dni_admin,usuario_admin, contrasena_admin, "admin")
    adm.save()
    usu.save()
    noti = True
    return render(request, 'moduloRoot_crearAdmin.html', {"nombre":nombre, "noti":noti})

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
    cli = Cliente(dni_usuario,usuario_usuario, contrasena_usuario, "cliente", nombre_usuario, apellido_usuario, dni_usuario, fecha_usuario, lugar_usuario, direccion_usuario, sexo_usuario, correo_usuario, " ", " ", False, False, False, " ", " ")
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

def moduloAdmin_Libro_Crear2(request):
    nombre = "Crear Libro"
    if request.POST:
        caratula_libro = request.FILES.get('foto')
        autor_libro = request.POST.get ('autor')
        desc_libro = request.POST.get('descripcion')
        titulo_libro = request.POST.get('titulo')
        genero_libro = request.POST.get('genero')
        editorial_libro = request.POST.get('editorial')
        nroP_libro = request.POST.get('nroP')
        precio_libro = request.POST.get('precio')
        issn_libro = request.POST.get('isnn')
        idioma_libro = request.POST.get('idioma')
        estado_libro = request.POST.get('estado')
        categoria_libro = request.POST.get('categoria')
        fechaP_libro = request.POST.get('fechaP')
        fechaL_libro = request.POST.get('fechaL')
        libro = Libro(titulo_libro, autor_libro, desc_libro, genero_libro, editorial_libro, nroP_libro, precio_libro, issn_libro, idioma_libro, estado_libro, categoria_libro, fechaP_libro, fechaL_libro, caratula_libro)
        libro.save()
    noti = True
    return render(request, 'moduloAdmin_Libro_Crear.html', {"nombre":nombre, "noti":noti})

def moduloAdmin_Libro_Modificar(request):
    nombre = "Modificar Libro"
    return render(request, 'moduloAdmin_Libro_Modificar.html', {"nombre":nombre})

def moduloAdmin_Libro_Modificar2(request):
    nombre = "Modificar Libro"
    issn = request.GET["issn"]
    lib = Libro.objects.filter(ISSN = issn)
    caratula_libro = lib[0].caratula
    autor_libro = lib[0].autor
    desc_libro = lib[0].descripcion
    titulo_libro = lib[0].titulo
    genero_libro = lib[0].genero
    editorial_libro = lib[0].editorial
    nroP_libro = lib[0].nroPaginas
    precio_libro = lib[0].precio
    issn_libro = lib[0].ISSN
    idioma_libro = lib[0].idioma
    estado_libro = lib[0].estado
    categoria_libro = lib[0].categoria
    fechaP_libro = lib[0].fechaPublicacion
    fechaL_libro = lib[0].fechaLanzamiento
    return render(request, 'moduloAdmin_Libro_Modificar.html', {"titulo_libro": titulo_libro, "autor_libro": autor_libro, "desc_libro": desc_libro, "genero_libro": genero_libro, "editorial_libro": editorial_libro, "nroP_libro": nroP_libro, "precio_libro": precio_libro, "issn_libro": issn_libro, "idioma_libro": idioma_libro, "estado_libro": estado_libro, "categoria_libro": categoria_libro, "fechaP_libro": fechaP_libro, "fechaL_libro": fechaL_libro, "caratula_libro": caratula_libro})

def moduloAdmin_Libro_Modificar3(request):
    nombre = "Modificar Libro"
    if request.POST:
        caratula_libro = request.FILES.get('foto')
        autor_libro = request.POST.get ('autor')
        desc_libro = request.POST.get('descripcion')
        titulo_libro = request.POST.get('titulo')
        genero_libro = request.POST.get('genero')
        editorial_libro = request.POST.get('editorial')
        nroP_libro = request.POST.get('nroP')
        precio_libro = request.POST.get('precio')
        issn_libro = request.POST.get('isnn')
        idioma_libro = request.POST.get('idioma')
        estado_libro = request.POST.get('estado')
        categoria_libro = request.POST.get('categoria')
        fechaP_libro = request.POST.get('fechaP')
        fechaL_libro = request.POST.get('fechaL')
        libro = Libro(titulo_libro, autor_libro, desc_libro, genero_libro, editorial_libro, nroP_libro, precio_libro, issn_libro, idioma_libro, estado_libro, categoria_libro, fechaP_libro, fechaL_libro, caratula_libro)
        libro.save()
    noti = True
    return render(request, 'moduloAdmin_Libro_Modificar.html', {"nombre":nombre, "noti": noti})

def moduloAdmin_Libro_Listar(request):
    nombre = "Listar Libros"
    return render(request, 'moduloAdmin_Libro_Listar.html', {"nombre":nombre})

def moduloAdmin_Libro_Buscar(request):
    nombre = "Buscar Libro"
    return render(request, 'moduloAdmin_Libro_Buscar.html', {"nombre":nombre})

def moduloAdmin_Libro_Eliminar(request):
    nombre = "Eliminar Libro"
    return render(request, 'moduloAdmin_Libro_Eliminar.html', {"nombre":nombre})

def moduloAdmin_Libro_Eliminar2(request):
    nombre = "Eliminar Libro"
    issn = request.GET["issn"]
    lib = Libro.objects.filter(ISSN = issn)
    caratula_libro = lib[0].caratula
    autor_libro = lib[0].autor
    desc_libro = lib[0].descripcion
    titulo_libro = lib[0].titulo
    genero_libro = lib[0].genero
    editorial_libro = lib[0].editorial
    nroP_libro = lib[0].nroPaginas
    precio_libro = lib[0].precio
    issn_libro = lib[0].ISSN
    idioma_libro = lib[0].idioma
    estado_libro = lib[0].estado
    categoria_libro = lib[0].categoria
    fechaP_libro = lib[0].fechaPublicacion
    fechaL_libro = lib[0].fechaLanzamiento
    return render(request, 'moduloAdmin_Libro_Eliminar.html', {"titulo_libro": titulo_libro, "autor_libro": autor_libro, "desc_libro": desc_libro, "genero_libro": genero_libro, "editorial_libro": editorial_libro, "nroP_libro": nroP_libro, "precio_libro": precio_libro, "issn_libro": issn_libro, "idioma_libro": idioma_libro, "estado_libro": estado_libro, "categoria_libro": categoria_libro, "fechaP_libro": fechaP_libro, "fechaL_libro": fechaL_libro, "caratula_libro": caratula_libro})

def moduloAdmin_Libro_Eliminar3(request):
    nombre = "Eliminar Libro"
    issn = request.GET["issn"]
    lib = Libro.objects.filter(ISSN = issn)
    lib.delete()
    noti = True
    return render(request, 'moduloAdmin_Libro_Eliminar.html', {"nombre":nombre, "noti": noti})

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
    try:
        perfil = usuario_global[2]
        if perfil:
            noti= True
    except:
        noti = False
    return render(request, 'moduloUsuario.html', {"nombre":nombre, "perfil":perfil})

def moduloUsuario_Usuario_Modificar(request):
    nombre = "Modificar Usuario"
    cli = Cliente.objects.filter(usuario = usuario_global[0], contrasena = usuario_global[1])
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

def moduloUsuario_Usuario_Modificar2(request):
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
    cli = Cliente(dni_usuario,usuario_usuario, contrasena_usuario, "cliente", nombre_usuario, apellido_usuario, dni_usuario, fecha_usuario, lugar_usuario, direccion_usuario, sexo_usuario, correo_usuario, cliente_global[0],cliente_global[1],cliente_global[2],cliente_global[3],cliente_global[4],cliente_global[5],cliente_global[6])
    usu = Usuario(dni_usuario,usuario_usuario, contrasena_usuario, "cliente")
    cli.save()
    usu.save()
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
    if request.POST:
        foto_usuario = request.FILES.get('foto')
        desc_usuario = request.POST.get('comentario')
        perfil_usuario = True
        try:
            noti_usuario = request.POST.get('noti')
            if noti_usuario:
                noti= True
        except:
            noti = False

        try:    
            msj_usuario = request.POST.get('msj')
            if msj_usuario:
                msj= True
        except:
            msj = False


        clinuevo = Cliente(cli[0].dni, cli[0].usuario, cli[0].contrasena, cli[0].tipo, cli[0].nombres, cli[0].apellidos, cli[0].dni, cli[0].fechaN, cli[0].lugarN, cli[0].direccion, cli[0].genero, cli[0].correo, " ", " ", noti, msj, perfil_usuario, foto_usuario, desc_usuario)
        clinuevo.save()
    
    return HttpResponseRedirect("https://tleladn.herokuapp.com/moduloUsuario/") 

def moduloUsuario_Perfil_Modificar(request):
    nombre = "Modificar Perfil"
    cli = Cliente.objects.filter(usuario = usuario_global[0], contrasena = usuario_global[1])
    if cli:
        suscripcion = cli[0].suscripcion
        mensajeria = cli[0].mensajeria
        foto = cli[0].foto
        descripcion = cli[0].descripcion
    else: 
        pass
    return render(request, 'moduloUsuario_Perfil_Modificar.html', {"nombre":nombre, "suscripcion":suscripcion,"mensajeria":mensajeria,"foto":foto,"descripcion":descripcion})

def moduloUsuario_Perfil_Modificar2(request):
    nombre = "Modificar Perfil"
    cli = Cliente.objects.filter(usuario = usuario_global[0], contrasena = usuario_global[1])
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
        temas_usuario = cli[0].temas
        top_usuario = cli[0].top
        perfil_usuario = cli[0].perfil    
        foto_usuario = request.POST.get('foto')
        desc_usuario = request.POST.get('comentario')
        try:
            noti_usuario = request.POST.get('noti')
            if noti_usuario:
                noti= True
        except:
            noti = False

        try:    
            msj_usuario = request.POST.get('msj')
            if msj_usuario:
                msj= True
        except:
            msj = False
        else:
            pass
    cli = Cliente(dni_usuario,usuario_usuario, contrasena_usuario, "cliente", nombre_usuario, apellido_usuario, dni_usuario, fecha_usuario, lugar_usuario, direccion_usuario, sexo_usuario, correo_usuario, temas_usuario, top_usuario, noti, msj, perfil_usuario, foto_usuario, desc_usuario)
    cli.save()
    notif = True
    return render(request, 'moduloUsuario_Perfil_Modificar.html', {"nombre":nombre, "noti":notif})

def moduloUsuario_Perfil_Eliminar(request):
    nombre = "Eliminar Perfil"
    cli = Cliente.objects.filter(usuario = usuario_global[0], contrasena = usuario_global[1])
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
        temas_usuario = cli[0].temas
        top_usuario = cli[0].top
        perfil_usuario = False
    else:
        pass
    cli = Cliente(dni_usuario,usuario_usuario, contrasena_usuario, "cliente", nombre_usuario, apellido_usuario, dni_usuario, fecha_usuario, lugar_usuario, direccion_usuario, sexo_usuario, correo_usuario, temas_usuario, top_usuario, False, False, perfil_usuario, " ", " ")
    cli.save()
    return HttpResponseRedirect("https://tleladn.herokuapp.com/moduloUsuario/") 

def moduloUsuario_Usuario_Mensajeria(request):
    nombre = "Modificar Usuario"
    return render(request, 'moduloUsuario_Usuario_Mensajeria.html', {"nombre":nombre})