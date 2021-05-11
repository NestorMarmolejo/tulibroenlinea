from django.db import models

'''
class Persona(models.Model):

    nombres = models.CharField(max_length = 20)
    apellidos = models.CharField(max_length = 20)
    dni = models.IntegerField()
    fechaN = models.DateField()
    lugarN = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 10)
    correo = models.EmailField()
    temas = models.CharField(max_length = 30)
'''
class Usuario(models.Model):

    idUsuario = models.CharField(max_length = 10, primary_key = True)
    usuario = models.CharField(max_length = 10)
    contrasena = models.CharField(max_length = 10)
    tipo = models.CharField(max_length = 10)

class Administrador(models.Model):

    idUsuario = models.CharField(max_length = 10, primary_key = True)
    usuario = models.CharField(max_length = 10)
    contrasena = models.CharField(max_length = 10)
    tipo = models.CharField(max_length = 10)
        
class Root(models.Model):

    idUsuario = models.CharField(max_length = 10, primary_key = True)
    usuario = models.CharField(max_length = 10)
    contrasena = models.CharField(max_length = 10)
    tipo = models.CharField(max_length = 10)

class Cliente(models.Model):

    idUsuario = models.CharField(max_length = 10, primary_key = True)
    usuario = models.CharField(max_length = 10)
    contrasena = models.CharField(max_length = 10)
    tipo = models.CharField(max_length = 10)


    nombres = models.CharField(max_length = 20)
    apellidos = models.CharField(max_length = 20)
    dni = models.CharField(max_length = 10)
    fechaN = models.DateField()
    lugarN = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 10)
    correo = models.EmailField()
    temas = models.CharField(max_length = 30)


    top = models.CharField(max_length = 30)
    suscripcion = models.BooleanField()
    mensajeria = models.BooleanField()

class Libro(models.Model):
    
    titulo = models.CharField(max_length = 20)
    escritor = models.CharField(max_length = 20)
    anho = models.CharField(max_length = 4)
    genero = models.CharField(max_length = 10)
    editorial = models.CharField(max_length = 10)
    nroPaginas = models.CharField(max_length = 4)
    precio = models.IntegerField()
    ISSN = models.CharField(max_length = 20, primary_key = True)
    idioma = models.CharField(max_length = 10)
    estado = models.CharField(max_length = 10)
    categoria = models.CharField(max_length = 10)
    fechaPublicacion = models.DateField()

class Noticia(models.Model):

    nroNoticia = models.CharField(max_length = 10, primary_key = True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length = 30)

class Devolucion(models.Model):

    nroDevolucion = models.CharField(max_length = 20, primary_key = True)
    libro = models.CharField(max_length = 10)
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
    tipo = models.CharField(max_length = 10)
    montoBase = models.IntegerField()
    montoLimite = models.IntegerField()
    saldo = models.IntegerField()