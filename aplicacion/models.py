from django.db import models

'''
class Persona(models.Model):

    nombres = models.CharField(max_length = 20)
    apellidos = models.CharField(max_length = 20)
    dni = models.IntegerField()
    fechaN = models.DateField()
    lugarN = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 20)
    correo = models.EmailField()
    temas = models.CharField(max_length = 30)
'''
class Usuario(models.Model):

    idUsuario = models.CharField(max_length = 20, primary_key = True)
    usuario = models.CharField(max_length = 20)
    contrasena = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)

class Administrador(models.Model):

    idUsuario = models.CharField(max_length = 20, primary_key = True)
    usuario = models.CharField(max_length = 20)
    contrasena = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)

    nombres = models.CharField(max_length = 20)
    apellidos = models.CharField(max_length = 20)
    dni = models.CharField(max_length = 20)
    fechaN = models.DateField()
    lugarN = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 20)
    correo = models.EmailField()
        
class Root(models.Model):

    idUsuario = models.CharField(max_length = 20, primary_key = True)
    usuario = models.CharField(max_length = 20)
    contrasena = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)

class Cliente(models.Model):

    idUsuario = models.CharField(max_length = 20, primary_key = True)
    usuario = models.CharField(max_length = 20)
    contrasena = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)


    nombres = models.CharField(max_length = 20)
    apellidos = models.CharField(max_length = 20)
    dni = models.CharField(max_length = 20)
    fechaN = models.DateField()
    lugarN = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 20)
    correo = models.EmailField()
    temas = models.CharField(max_length = 30)


    top = models.CharField(max_length = 30)
    suscripcion = models.BooleanField()
    mensajeria = models.BooleanField()
    perfil = models.BooleanField()
    foto = models.ImageField(upload_to="fotos", null =True)
    descripcion = models.CharField(max_length = 100) 

class Libro(models.Model):
    
    titulo = models.CharField(max_length = 20)
    autor = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 120)
    genero = models.CharField(max_length = 20)
    editorial = models.CharField(max_length = 20)
    nroPaginas = models.CharField(max_length = 4)
    precio = models.IntegerField()
    ISSN = models.CharField(max_length = 20, primary_key = True)
    idioma = models.CharField(max_length = 20)
    estado = models.CharField(max_length = 20)
    categoria = models.CharField(max_length = 20)
    fechaPublicacion = models.DateField()
    fechaLanzamiento = models.DateField()
    caratula = models.ImageField(upload_to="caratulas", null =True)

class Noticia(models.Model):

    nroNoticia = models.CharField(max_length = 20, primary_key = True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length = 30)

class Devolucion(models.Model):

    nroDevolucion = models.CharField(max_length = 20, primary_key = True)
    libro = models.CharField(max_length = 20)
    fecha = models.DateField()
    motivo = models.CharField(max_length = 30)

class Compra(models.Model):

    nroCompra = models.CharField(max_length = 20, primary_key = True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()     

class Reserva(models.Model):

    nroReserva = models.CharField(max_length = 20, primary_key = True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

class Mensaje(models.Model):
 
    horaEnvio = models.TimeField()
    horaEntrega = models.TimeField()
    destinatario = models.CharField(max_length = 20)
    aprobacion = models.BooleanField()
    contenido = models.CharField(max_length = 30)

class Tarjeta(models.Model):

    nroTarjeta = models.CharField(max_length = 16, primary_key = True)
    cvv = models.IntegerField()
    fechaExpiracion = models.DateField()
    titular = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)
    montoBase = models.IntegerField()
    montoLimite = models.IntegerField()
    saldo = models.IntegerField()
