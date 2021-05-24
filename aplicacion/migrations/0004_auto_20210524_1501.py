# Generated by Django 3.2 on 2021-05-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_cliente_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='contrasena',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='idUsuario',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='usuario',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='contrasena',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idUsuario',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='lugarN',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='libro',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='libro',
            name='estado',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='libro',
            name='idioma',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='nroNoticia',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='root',
            name='contrasena',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='root',
            name='idUsuario',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='root',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='root',
            name='usuario',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(max_length=20),
        ),
    ]
