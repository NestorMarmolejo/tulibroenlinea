class Persona(object):
    def __init__(self, nombres, apellidos, dni, fechaN, lugarN, direccion, genero, correo, temas):

        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.fechaN = fechaN
        self.lugarN = lugarN
        self.direccion = direccion
        self.genero = genero
        self.correo = correo
        self.temas = temas

class Usuario(object):
    def __init__(self, idUsuario, usuario, contraseña, tipo):

        self.idUsuario = idUsuario
        self.usuario = usuario
        self.contraseña = contraseña
        self.tipo = tipo

class Administrador(Usuario):
    pass
        
class Root(Usuario):
    pass

class cliente(Usuario, Persona):
    def __init__(self, top, suscripcion):
        
        self.top = top
        self.suscripcion = suscripcion

class Libro(object):
    def __init__(self, titulo, escritor, anho, genero, editorial, nroPaginas, precio, ISSN, idioma, estado, categoria, fechaPublicacion):

        self.titulo = titulo
        self.escritor = escritor
        self.anho = anho
        self.genero = genero
        self.editorial = editorial
        self.nroPaginas = nroPaginas
        self.precio = precio
        self.ISSN = ISSN
        self.idioma = idioma
        self.estado = estado
        self.categoria = categoria
        self.fechaPublicacion = fechaPublicacion

class Noticia(object):
    def __init__(self, nroNoticia, fecha, descripcion):

        self.nroNoticia = nroNoticia
        self.fecha = fecha
        self.descripcion = descripcion

class Devolucion(object):
    def __init__(self, nroDevolucion, libro, fecha, motivo):

        self.nroDevolucion = nroDevolucion
        self.libro = libro
        self.fecha = fecha
        self.motivo = motivo

class Compra(object):
    def __init__(self, nroCompra, cantidad, subtotal):

        self.nroCompra = nroCompra
        self.cantidad = cantidad
        self.subtotal = subtotal     

class Reserva(object):
    def __init__(self, nroReserva, cantidad, subtotal):

        self.nroReserva = nroReserva
        self.cantidad = cantidad
        self.subtotal = subtotal

class Mensaje(object):
    def __init__(self, horaEnvio, horaEntrega, fechaEnvio, destinatario, aprobacion, contenido):
        
        self.horaEnvio = horaEnvio
        self.horaEntrega = horaEntrega
        self.destinatario = destinatario
        self.aprobacion = aprobacion
        self.contenido = contenido

class Tarjeta(object):
    def __init__(self, nroTarjeta, cvv, fechaExpiracion, titular, tipo, montoBase, montoLimite, saldo):

        self.nroTarjeta = nroTarjeta
        self.cvv = cvv
        self.fechaExpiracion = fechaExpiracion
        self.titular = titular
        self.tipo = tipo
        self.montoBase = montoBase
        self.montoLimite = montoLimite
        self.saldo = saldo
