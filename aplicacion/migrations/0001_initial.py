# Generated by Django 3.2 on 2021-05-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.CharField(max_length=10)),
                ('usuario', models.CharField(max_length=10)),
                ('contrasena', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.CharField(max_length=10)),
                ('usuario', models.CharField(max_length=10)),
                ('contrasena', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('dni', models.IntegerField()),
                ('fechaN', models.DateField()),
                ('lugarN', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('temas', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('suscripcion', models.BooleanField()),
                ('mensajeria', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroCompra', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroDevolucion', models.CharField(max_length=20)),
                ('libro', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('motivo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('escritor', models.CharField(max_length=20)),
                ('anho', models.CharField(max_length=4)),
                ('genero', models.CharField(max_length=10)),
                ('editorial', models.CharField(max_length=10)),
                ('nroPaginas', models.CharField(max_length=4)),
                ('precio', models.IntegerField()),
                ('ISSN', models.CharField(max_length=20)),
                ('idioma', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=10)),
                ('categoria', models.CharField(max_length=10)),
                ('fechaPublicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaEnvio', models.TimeField()),
                ('horaEntrega', models.TimeField()),
                ('destinatario', models.CharField(max_length=20)),
                ('aprobacion', models.BooleanField()),
                ('contenido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroNoticia', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroReserva', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.CharField(max_length=10)),
                ('usuario', models.CharField(max_length=10)),
                ('contrasena', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroTarjeta', models.CharField(max_length=16)),
                ('cvv', models.IntegerField()),
                ('fechaExpiracion', models.DateField()),
                ('titular', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=10)),
                ('montoBase', models.IntegerField()),
                ('montoLimite', models.IntegerField()),
                ('saldo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.CharField(max_length=10)),
                ('usuario', models.CharField(max_length=10)),
                ('contrasena', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
    ]
